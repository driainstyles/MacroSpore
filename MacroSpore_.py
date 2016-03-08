from ij import IJ,ImagePlus,ImageStack
from ij.process import FloatProcessor

imp = IJ.getImage()
print imp

# Print image details  
print "title:", imp.title  
print "width:", imp.width  
print "height:", imp.height  
print "number of pixels:", imp.width * imp.height  
print "number of slices:", imp.getNSlices()  
print "number of channels:", imp.getNChannels()  
print "number of time frames:", imp.getNFrames()  
  
types = {ImagePlus.COLOR_RGB : "RGB",  
         ImagePlus.GRAY8 : "8-bit",  
         ImagePlus.GRAY16 : "16-bit",  
         ImagePlus.GRAY32 : "32-bit",  
         ImagePlus.COLOR_256 : "8-bit color"}  
  
print "image type:", types[imp.type]
# Get the color processor of the image and extract the channels.
cp = imp.getProcessor()
red = cp.toFloat(0,None)
green = cp.toFloat(1,None)
blue = cp.toFloat(2,None)

#print rchannel
red_image = ImagePlus("Red channel",red)
#IJ.setAutoThreshold(red_image,"Otsu dark")
green_image = ImagePlus("Green channel", green)
blue_image = ImagePlus("Blue channel", blue)
red_image.show()
green_image.show()
blue_image.show()