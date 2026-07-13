import os
from PIL import Image

def optimize_image(filepath, category):
    try:
        img = Image.open(filepath)
        
        # Determine target size based on category
        if category == 'hero':
            target_size = (1920, 1080)
            max_kb = 500
        elif category == 'category':
            target_size = (800, 600)
            max_kb = 250
        else: # product
            target_size = (800, 800)
            max_kb = 150
            
        # Resize image using thumbnail to maintain aspect ratio but ensure it's not too huge
        img.thumbnail((target_size[0], target_size[1]), Image.Resampling.LANCZOS)
        
        # Save as WebP
        webp_path = filepath.rsplit('.', 1)[0] + '.webp'
        quality = 80
        
        while True:
            img.save(webp_path, 'WEBP', quality=quality)
            size_kb = os.path.getsize(webp_path) / 1024
            
            if size_kb <= max_kb or quality <= 40:
                break
                
            quality -= 10
            
        print(f"Optimized {filepath} -> {webp_path} ({size_kb:.1f} KB, Quality: {quality})")
        
        # Remove original jpg
        if os.path.exists(webp_path):
            os.remove(filepath)
            
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

def process_directory():
    base_dir = 'assets/images'
    
    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                filepath = os.path.join(root, file)
                
                # Determine category
                if 'hero' in file or 'contact' in file or 'about' in file:
                    cat = 'hero'
                elif 'category' in file:
                    cat = 'category'
                else:
                    cat = 'product'
                    
                optimize_image(filepath, cat)

if __name__ == '__main__':
    process_directory()
    print("Optimization complete.")
