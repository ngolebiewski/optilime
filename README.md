# Optilime 🍋‍🟩
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
- [] Experiment with and learn tkinter through documentation. Make button, open files, show images, etc.
- [] Write Pillow functions for transforming images and tests using pytest. This will be an issue with many sub issues. Use rawpy library to add in Pillow functionality for camera raw files.
- [] Write ffmpeg scripts for .mov and .mpf to animated gif processing flows. Stretch: images to mov flows.
- [] Make GUI in tkinter to see, preview and edit/transform images.
- [] Bundle with pyintstaller(?) to be stand alone MacOSx and Linux(?) desktop app and release. 

## TECH
- Pytest: Testing
- Pillow: Image processing