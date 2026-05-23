from PIL import Image
import os, sys
import rawpy
from pillow_heif import register_heif_opener
from constants import RAW_EXTENSIONS

# This enables the program to read iPhone specific HEIF files
register_heif_opener()

def main():
    print("PILLOW image processor wrapper")
    img_to_web_jpg("./sample_images/snes-controller.png","high", (300,100),'BILINEAR', bg_color=(100,200,255))
    img_to_web_jpg("./sample_images/iphone_art_ribbon.HEIC","medium", (1000,1000))
    img_to_web_jpg("./sample_images/aurora.ARW","maximum", (2000,2000),"BILINEAR")
    img_to_web_jpg("./sample_images/not_a_real_image.ARW","maximum", (2000,2000),"BILINEAR")

# For a first image related function, lets just resize a jpg for the web, and also use the quality
def img_to_web_jpg(infile, quality="maximum", new_size=(-1,-1), resample="LANCZOS", bg_color = (200, 200, 200)):
    # https://pillow.readthedocs.io/en/stable/reference/JpegPresets.html
    # The following presets are available by default: web_low, web_medium, web_high, web_very_high, web_maximum, low, medium, high, maximum
    f, e = os.path.splitext(infile)
    print(new_size,quality)

    outfile = f + "_web" + ".jpg"
    try:
        with open_any_image(infile) as img:
            # for PNGs tests for the alpha/transparency layer.
            if img.mode in ("RGBA", "P"):
                if img.mode == "P":
                    img = img.convert("RGBA")
                bg_color = bg_color 
                background = Image.new("RGB", img.size, bg_color)
    
                # 2. Paste the original image onto it. 
                # The 3rd argument 'img' acts as the transparency mask (alpha channel)
                background.paste(img, (0, 0), img)
                
                # 3. Swap our reference to the newly flattened image
                img = background
            elif img.mode != "RGB":
                # Fallback for grayscale or other odd formats without transparency
                img = img.convert("RGB")
                
            # Resize if new_size params set. 
            # Ref: https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.resize
            # this could be a good stand alone function that we can test in pytest!
            if new_size != (-1,-1):
                # may need to do a check here to make sure that we are keeping the original ratio of the image.
                og_w, og_h = img.width, img.height
                new_w, new_h = new_size
                print(new_w,'<- W |new| H ->',new_h)
                
                # Check resize ratio
                diff = .01
                og_ratio = og_w / og_h
                new_ratio = new_w / new_h
                
                if abs(og_ratio - new_ratio) > diff:
                    print("image ratio does not match, OG: ",og_w / og_h,"NEW: ", new_ratio)
                    # Do some math to clamp to the larger new dimension and adjust the other accordings.
                    if og_ratio > new_ratio:
                        new_h = int(new_w / og_ratio)
                    else:
                        new_w = int(new_h * og_ratio)
                        

                filter_enum = getattr(Image.Resampling, resample, Image.Resampling.LANCZOS)
                img = img.resize((new_w, new_h), resample=filter_enum)
            
            # How do we specify where to save?
            img.save(outfile, quality=quality)
    except OSError as e:
        print("cannot convert", infile)
        print("error: ", e)

def open_any_image(infile):
    '''
    A robust function for opening ANY format image file, so that the our code can work with it.
    Works with jpg, png, gif, TIFF, RAW files (via rawpy), and HEIF which are native to iPhones.
    '''
    
    # Make sure this is a valid path
    if not os.path.exists(infile):
        raise FileNotFoundError("File not found: ", infile)
    
    _, ext = os.path.splitext(infile.lower())
    
    if ext in RAW_EXTENSIONS:
        print("Processing RAW file: ", {infile})
        with rawpy.imread(infile) as raw: 
            # postprocess() extracts the raw pixels into a NumPy RGB array
            rgb_array = raw.postprocess()
            # Convert the raw pixel array directly into a native Pillow Image
            return Image.fromarray(rgb_array)
    else:
        # Handles standard types (PNG, JPG, TIFF, etal.) and HEIC via the registered plugin pillow+heif
        print("Opening standard/HEIC image via Pillow: ", infile)
        img = Image.open(infile)
        img.load() 
        return img

if __name__ == "__main__":
    main()