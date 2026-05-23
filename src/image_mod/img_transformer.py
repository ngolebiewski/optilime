from PIL import Image
import os, sys
from pillow_heif import register_heif_opener
register_heif_opener()

def main():
    print("PILLOW image processor wrapper")
    img_to_web_jpg("./snes-controller.png","high", (300,100),'BILINEAR', bg_color=(100,200,255))
    img_to_web_jpg("./sample_images/iphone_art_ribbon.HEIC","medium", (1000,1000))

# For a first image related function, lets just resize a jpg for the web, and also use the quality
def img_to_web_jpg(infile, quality="maximum", new_size=(-1,-1), resample="LANCZOS", bg_color = (200, 200, 200)):
    # https://pillow.readthedocs.io/en/stable/reference/JpegPresets.html
    # The following presets are available by default: web_low, web_medium, web_high, web_very_high, web_maximum, low, medium, high, maximum
    f, e = os.path.splitext(infile)
    print(new_size,quality)

    outfile = f + "_web" + ".jpg"
    try:
        with Image.open(infile) as img:
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
            
            img.save(outfile, quality=quality)
    except OSError as e:
        print("cannot convert", infile)
        print("error: ", e)

def open_any_image(infile):
    '''
    This should be a robust function for opening ANY format image file, so that the tesr of our code can work with it.
    This should work with jpg, png, gif, TIFF, RAW files (via rawpy), and HEIF which are native to iPhones.
    '''
    pass

if __name__ == "__main__":
    main()