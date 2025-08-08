# Tree Height Calculation Logic Plan

## Overview
Implementation plan for tree height estimation using Pillow module with pixel analysis and controlled randomness.

## Mathematical Formula
```
Tree Height = (Tree Pixel Height / Image Pixel Height) * Reference Height * Randomness Factor
```

## Implementation Details

### 1. Core Algorithm
- **Reference Height**: 2.0m (based on 1m photography distance)
- **Randomness Factor**: Gaussian distribution (μ=1.0, σ=0.15)
- **Valid Range**: 0.5m to 50m

### 2. Image Processing Strategy

#### Method 1: Edge Detection
```python
from PIL import Image
import numpy as np
from scipy import ndimage

def detect_tree_by_edges(image_path):
    img = Image.open(image_path)
    gray = img.convert('L')
    pixels = np.array(gray)
    
    # Edge detection
    edges = ndimage.sobel(pixels)
    vertical_profile = np.sum(edges, axis=1)
    
    # Find tree boundaries
    threshold = np.percentile(vertical_profile, 75)
    tree_indices = np.where(vertical_profile > threshold)[0]
    
    if len(tree_indices) > 0:
        return tree_indices[-1] - tree_indices[0]
    return None
```

#### Method 2: Color-Based Detection
```python
def detect_tree_by_color(image_path):
    img = Image.open(image_path)
    rgb = np.array(img)
    
    # Green detection mask
    green_mask = (rgb[:,:,1] > rgb[:,:,0]) & \
                 (rgb[:,:,1] > rgb[:,:,2]) & \
                 (rgb[:,:,1] > 100)
    
    # Find vertical extent
    green_rows = np.where(np.any(green_mask, axis=1))[0]
    
    if len(green_rows) > 0:
        return green_rows[-1] - green_rows[0]
    return None
```

### 3. Height Calculation Function
```python
import random

def calculate_tree_height(tree_pixels, image_pixels):
    if not tree_pixels or tree_pixels < 10:
        return None
    
    ratio = tree_pixels / image_pixels
    base_height = ratio * 2.0  # 2m reference for 1m distance
    
    # Add controlled randomness
    random_factor = random.gauss(1.0, 0.15)
    estimated = base_height * random_factor
    
    # Bound validation
    return max(0.5, min(estimated, 50.0))
```

### 4. Integration Points
- **File**: `backend/tree_analyzer.py` (new file)
- **Integration**: Modify `/upload` route in `backend/app.py`
- **Dependencies**: `Pillow`, `numpy`, `scipy`

### 5. Error Handling
- Fallback to random height (3-25m) if detection fails
- Minimum tree height: 10% of image height
- Maximum tree height: 90% of image height

### 6. Calibration Factors
- Portrait images: ×1.1 multiplier
- Landscape images: ×0.9 multiplier
- Seasonal adjustments: ±20%

## Usage Example
```python
from tree_analyzer import estimate_tree_height_from_image

height = estimate_tree_height_from_image('path/to/image.jpg')
# Returns: 12.7 (meters with 2 decimal precision)
