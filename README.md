# 📸 Optilime 🍋‍🟩
## Image Resizer Desktop Program

** NOTE: NO GENERATIVE AI HAS OR WILL BE USED IN THIS PROJECT **

** THIS IS THE FINAL PROJECT FOR HARVARD CS50P **

I am tired of paying for my Photoshop susbcription -- and I have a friend that I am making a website for who is an artist. They don't have a good tool for resizing images, and I could use one too! I find that I write many small PILLOW scripts that do one thing, then when I go back, if I CAN find it, it is janky.

Basically, I want to go for a 1990s DOS aesthetic, and have a 2-up thing going on, that can batch process or individual process.

Kind of like a 90s graphical wrapper for PILLOW meets modern Photoshop, and where you don't need to upload 1GB scans of artwork to the web to get processed. 

## STRETCH GOALS

- Integration to get your images off of Instagram
- Integration to get your images off of TBD
- Video to GIF integration with FFMPEG

## RESEARCH

I have heard of tkinter, i also thought about using Curses or Textable for a Terminal User Interface, but as it is graphics and a main compoinent is seeing the images, I feel like those would not be as ideal as they are more text bases and to show images, you would need bespoke terminals, and that is too much to ask of any user to install.


https://docs.python.org/3/library/tkinter.html

With tkinter, I like how it is part of Python's built-in library. A more robust GUI framework would inevitable abstract the process more, and I like this being as close to Python as possible. Out of scopre would be writing directly in C to interface with Apple's Metal Graphics library and to get as close to the hardware as possible, although that does sound like fun. 

Eventually, I want to try and bundle this as an app, so may have to go into XCode territory and finally pay that $99 Annual fee to Apple to become a developer that can sign for an app that doesn't get the "WARNING THIS WAS DOWNLOADED FROM THE INTERNET" error. 

## NOTES
- Use a lime as the imagery. Optics + Lime...

## PLAN
- [x] Experiment with and learn tkinter through documentation. Make button, open files, show images, etc. Note, may need to explore Pyside6 as an alternate desktop GUI option. 
- [ ] Write Pillow functions for transforming images and tests using pytest. This will be an issue with many sub issues. Use rawpy library to add in Pillow functionality for camera raw files. 
- [ ] Write ffmpeg scripts for .mov and .mpf to animated gif processing flows. Stretch: images to mov flows.
- [ ] Make GUI in tkinter to see, preview and edit/transform images. Pillow has a tk
- [ ] Bundle with pyintstaller(?) to be stand alone MacOSx and Linux(?) desktop app and release. 

## TECH
- [Pytest](https://docs.pytest.org/en/stable/): Testing
- [Pillow](https://pillow.readthedocs.io/en/stable/): Image processing
    - *Plugins*
        - [pillow-heif](https://pypi.org/project/pillow-heif/): Python bindings to libheif for working with HEIF images.
        - [Raw Py](https://letmaik.github.io/rawpy/index.html) and [Numpy](numpy.org): Import raw image files from fancy cameras
- [Departure Mono](https://departuremono.com/): Open source font, "a monospaced pixel font with a lo-fi technical vibe" -- **My favorite font**

## DEV NOTES

### tkinter
- While setting up the app, I started to think about the architecture, and landed on dividing the GUI into its own folder/module and then the same for the image processing side of things. 

- Finding that it is really unresponsive and flaky on my mac, for a simple test with a button that just changes text. Is it the virtual environment? Or just Tkinter?

### Pillow and image processing in 📂 image_mod
- Note, I a made all of the images that are in the test image folder. The Sony raw file is fairly large, you are warned.
- Constants file for things like raw photo extension types, etc.
- img_transformer.py
    - This is where the functions are kept
    - file opener (handles regular and raw)
    - image to web jpeg as the first feature

### Make requirements file
`pip freeze > requirements.txt`
