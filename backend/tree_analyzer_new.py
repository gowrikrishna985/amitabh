import os
import numpy as np
from PIL import Image
import logging
import cv2
from scipy import ndimage

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PreciseTreeAnalyzer:
    """Advanced tree height analyzer with improved precision."""
    
    def __init__(self):
        self.min_tree_height_pixels = 50
        
    def detect_reference_object(self, image_path, reference_type='person', expected_height=1.7):
        """Detect reference objects for scale calibration."""
        try:
            img = cv2.imread(image_path)
            if img is None:
                return None
                
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            
            if reference_type == 'person':
                # Skin tone detection
                lower_skin = np.array([0, 20, 70], dtype=np.uint8)
                upper_skin = np.array([20, 255, 255], dtype=np.uint8)
                skin_mask = cv2.inRange(hsv, lower_skin, upper_skin)
                
                contours, _ = cv2.findContours(skin_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                
                if contours:
                    largest_contour = max(contours, key=cv2.contourArea)
                    x, y, w, h = cv2.boundingRect(largest_contour)
                    
                    if h > img.shape[0] * 0.1 and w < img.shape[1] * 0.3:
                        return h
            
            elif reference_type == 'ruler':
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                edges = cv2.Canny(gray, 50, 150)
                
                lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=100, maxLineGap=10)
                
                if lines is not None:
                    for line in lines:
                        x1, y1, x2, y2 = line[0]
                        if abs(x2 - x1) < 10:
                            return abs(y2 - y1)
            
            return None
            
        except Exception as e:
            logger.error(f"Reference object detection failed: {e}")
            return None
    
    def advanced_edge_detection(self, image_path):
        """Enhanced edge detection with noise filtering."""
        try:
            img = Image.open(image_path)
            gray = img.convert('L')
            pixels = np.array(gray)
            
            # Apply Gaussian blur
            from scipy.ndimage import gaussian_filter
            blurred = gaussian_filter(pixels, sigma=1)
            
            # Sobel edge detection
            edges_x = ndimage.sobel(blurred, axis=1)
            edges_y = ndimage.sobel(blurred, axis=0)
            edges = np.sqrt(edges_x**2 + edges_y**2)
            
            # Clean up edges
            from scipy.ndimage import binary_erosion, binary_dilation
            edge_mask = edges > np.percentile(edges, 85)
            cleaned_edges = binary_erosion(binary_dilation(edge_mask))
            
            vertical_profile = np.sum(cleaned_edges, axis=1)
            vertical_profile = gaussian_filter(vertical_profile, sigma=2)
            
            # Find peaks
            from scipy.signal import find_peaks
            peaks, _ = find_peaks(vertical_profile, height=np.percentile(vertical_profile, 70))
            
            if len(peaks) >= 2:
                tree_height = peaks[-1] - peaks[0]
                if tree_height > self.min_tree_height_pixels:
                    return tree_height
            
            return None
            
        except Exception as e:
            logger.error(f"Advanced edge detection failed: {e}")
            return None
    
    def advanced_color_detection(self, image_path):
        """Enhanced color detection with better foliage identification."""
        try:
            img = Image.open(image_path)
            rgb = np.array(img)
            
            # Convert to HSV
            import colorsys
            hsv_data = []
            for row in rgb:
                hsv_row = []
                for pixel in row:
                    h, s, v = colorsys.rgb_to_hsv(pixel[0]/255, pixel[1]/255, pixel[2]/255)
                    hsv_row.append([h, s, v])
                hsv_data.append(hsv_row)
            
            hsv = np.array(hsv_data)
            h, s, v = hsv[:,:,0], hsv[:,:,1], hsv[:,:,2]
            
            # Green detection
            green_mask = ((h >= 0.25) & (h <= 0.45) &
                         (s >= 0.3) & (s <= 1.0) &
                         (v >= 0.2) & (v <= 1.0))
            
            # Clean mask
            from scipy.ndimage import binary_erosion, binary_dilation
            clean_mask = binary_erosion(binary_dilation(green_mask.astype(int)))
            
            green_rows = np.where(np.any(clean_mask, axis=1))[0]
            
            if len(green_rows) > self.min_tree_height_pixels:
                from scipy.signal import find_peaks
                green_profile = np.sum(clean_mask, axis=1)
                peaks, _ = find_peaks(green_profile, height=np.max(green_profile) * 0.3)
                
                if len(peaks) >= 2:
                    return peaks[-1] - peaks[0]
                else:
                    return green_rows[-1] - green_rows[0]
            
            return None
            
        except Exception as e:
            logger.error(f"Advanced color detection failed: {e}")
            return None
    
    def calculate_precise_height(self, tree_pixels, image_height, reference_pixels=None, reference_height=1.7):
        """Calculate tree height using reference objects."""
        if not tree_pixels or tree_pixels < self.min_tree_height_pixels:
            return None
        
        if reference_pixels and reference_height > 0:
            # Use reference for precise scaling
            pixels_per_meter = reference_pixels / reference_height
            tree_height_meters = tree_pixels / pixels_per_meter
            
            # Perspective correction
            perspective_factor = 1.0 + (tree_pixels / image_height) * 0.1
            corrected_height = tree_height_meters * perspective_factor
            
            return max(1.0, min(corrected_height, 50.0))
        
        else:
            # Camera-based calculation
            sensor_height_mm = 3.0
            focal_length_mm = 4.0
            
            vertical_fov_rad = 2 * np.arctan(sensor_height_mm / (2 * focal_length_mm))
            vertical_fov_deg = np.degrees(vertical_fov_rad)
            
            angular_resolution = vertical_fov_deg / image_height
            tree_angular_size = tree_pixels * angular_resolution
            
            tree_ratio = tree_pixels / image_height
            
            # Distance estimation
            if tree_ratio < 0.05:
                estimated_distance = 40.0
            elif tree_ratio < 0.15:
                estimated_distance = 25.0
            elif tree_ratio < 0.3:
                estimated_distance = 15.0
            elif tree_ratio < 0.5:
                estimated_distance = 8.0
            else:
                estimated_distance = 5.0
            
            tree_height = 2 * estimated_distance * np.tan(np.radians(tree_angular_size / 2))
            calibration_factor = 1.2
            final_height = tree_height * calibration_factor
            
            return max(2.0, min(final_height, 45.0))
    
    def estimate_tree_height(self, image_path, reference_type='auto', reference_height=1.7):
        """Main function to estimate tree height with improved precision."""
        try:
            img = Image.open(image_path)
            width, height = img.size
            
            reference_pixels = None
            if reference_type != 'none':
                reference_pixels = self.detect_reference_object(
                    image_path,
                    reference_type='person' if reference_type == 'auto' else reference_type,
                    expected_height=reference_height
                )
            
            detection_methods = [
                self.advanced_edge_detection,
                self.advanced_color_detection
            ]
            
            detected_heights = []
            for method in detection_methods:
                result = method(image_path)
                if result is not None:
                    detected_heights.append(result)
            
            if not detected_heights:
                return self._enhanced_fallback(image_path, height)
            
            avg_tree_pixels = np.mean(detected_heights)
            actual_height = self.calculate_precise_height(
                avg_tree_pixels,
                height,
                reference_pixels,
                reference_height
            )
            
            if actual_height is None:
                return self._enhanced_fallback(image_path, height)
            
            return round(actual_height, 2)
            
        except Exception as e:
            logger.error(f"Height estimation failed: {e}")
            return self._enhanced_fallback(image_path, height)
    
    def _enhanced_fallback(self, image_path, image_height):
        """Enhanced fallback method when detection fails."""
        try:
            img = Image.open(image_path)
            rgb = np.array(img)
            green_pixels = np.sum((rgb[:,:,1] > rgb[:,:,0]) & 
                                (rgb[:,:,1] > rgb[:,:,2]) & 
                                (rgb[:,:,1] > 100))
            
            total_pixels = rgb.shape[0] * rgb.shape[1]
            green_ratio = green_pixels / total_pixels
            
            if green_ratio > 0.3:
                estimated_height = 15.0 + (green_ratio - 0.3) * 50
            elif green_ratio > 0.1:
                estimated_height = 8.0 + (green_ratio - 0.1) * 35
            else:
                estimated_height = 5.0 + green_ratio * 30
            
            return max(3.0, min(estimated_height, 35.0))
            
        except:
            return 12.5

# Create global analyzer instance
analyzer = PreciseTreeAnalyzer()

def estimate_tree_height_from_image(image_path, reference_type='auto', reference_height=1.7):
    """Public interface for tree height estimation."""
    return analyzer.estimate_tree_height(image_path, reference_type, reference_height)

def test_tree_analyzer():
    """Test the tree analyzer with sample images."""
    test_dir = os.path.join(os.path.dirname(__file__), '..', 'frontend', 'static', 'uploads')
    
    if os.path.exists(test_dir):
        for filename in os.listdir(test_dir):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                filepath = os.path.join(test_dir, filename)
                height = estimate_tree_height_from_image(filepath)
                print(f"Image: {filename} -> Estimated height: {height}m")
