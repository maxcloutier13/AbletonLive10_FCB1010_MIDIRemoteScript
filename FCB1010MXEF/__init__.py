#Embedded file name: /Users/versonator/Jenkins/live/output/mac_64_static/Release/python-bundle/MIDI Remote Scripts/Oxygen8v2/__init__.py
from .FCB1010MXEF import FCB1010MXEF


def create_instance(c_instance):
    """ The generic script can be customised by using parameters (see config.py). """
    #return GenericScript(c_instance, Live.MidiMap.MapMode.absolute, Live.MidiMap.MapMode.absolute, DEVICE_CONTROLS, TRANSPORT_CONTROLS, VOLUME_CONTROLS, TRACKARM_CONTROLS, BANK_CONTROLS, CONTROLLER_DESCRIPTIONS, MIXER_OPTIONS)
    #Fuck this generic bullshit. Let's try something.
    return FCB1010MXEF(c_instance)