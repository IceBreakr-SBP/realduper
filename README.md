# realduper
Arma 3 script that removes objects that share the same coordinates (3 decimal precision) no matter the scale or height.

Install/Use:
1. Create new folder P:\RealDuper
2. Export problematic layer from the TB to duper.txt and save it in the same folder
3. Run python realduper.py and file output.txt will be created with all the dupes that share the same coordinates x,y (up to 3 decimal precision) while completely ignoring scale and height of the object.
WARNING/NOTE: Be careful not to stack any walls or other objects on top of each other, use different layer name for 2nd, 3rd "floor" of objects as that is recommended anyway when you need to fix something later on.
4. Clear/delete old layer (make backup of course first) and import output.txt in the same empty layer to have cleaned up stuff ready.
5. Enjoy optimised Arma3 project ;)
