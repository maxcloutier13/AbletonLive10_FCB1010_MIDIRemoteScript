from __future__ import with_statement
import Live
from _Framework.ControlSurface import ControlSurface
from _Framework.Layer import Layer
from _Framework.InputControlElement import MIDI_CC_TYPE
from _Framework.SliderElement import SliderElement
from _Framework.EncoderElement import EncoderElement
from _Framework.ButtonElement import ButtonElement
from _Framework.ButtonMatrixElement import ButtonMatrixElement
from _Framework.MixerComponent import MixerComponent
from _Framework.DeviceComponent import DeviceComponent
from _Framework.TransportComponent import TransportComponent
from _Framework.DrumRackComponent import DrumRackComponent
from _Framework.SessionComponent import SessionComponent
from _Framework.MidiMap import MidiMap as MidiMapBase
from _Framework.MidiMap import make_button, make_encoder, make_slider
from _Framework.InputControlElement import MIDI_NOTE_TYPE, MIDI_CC_TYPE

class FCB1010MX(ControlSurface):

    def __init__(self, *a, **k):
        super(FCB1010MX, self).__init__(*a, **k)
        self.show_message("-----------------------= FCB1010MX_v0.1 LOADING - maxcloutier13 says hi =----------------------------------------------------------")
        self.log_message("-----------------------= FCB1010MX_v0.1 LOADING - maxcloutier13 says hi =----------------------------------------------------------")
        with self.component_guard():
            #It's on
            self.log_message("-->It is on")
            #Keeping everything nice and empty and mapable for now
            #Encoders to auto-map to devices -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            #self._Encoder0 = EncoderElement(MIDI_CC_TYPE,13,22, Live.MidiMap.MapMode.absolute, name='Encoder0')
            #self._Encoder1 = EncoderElement(MIDI_CC_TYPE,13,23, Live.MidiMap.MapMode.absolute, name='Encoder1')
            #self._Encoder2 = EncoderElement(MIDI_CC_TYPE,13,24, Live.MidiMap.MapMode.absolute, name='Encoder2')
            #self._Encoder3 = EncoderElement(MIDI_CC_TYPE,13,25, Live.MidiMap.MapMode.absolute, name='Encoder3')
            #self._Encoder4 = EncoderElement(MIDI_CC_TYPE,13,26, Live.MidiMap.MapMode.absolute, name='Encoder4')
            #self._Encoder5 = EncoderElement(MIDI_CC_TYPE,13,27, Live.MidiMap.MapMode.absolute, name='Encoder5')
            #self._Encoder6 = EncoderElement(MIDI_CC_TYPE,13,28, Live.MidiMap.MapMode.absolute, name='Encoder6')
            #self._Encoder7 = EncoderElement(MIDI_CC_TYPE,13,29, Live.MidiMap.MapMode.absolute, name='Encoder7')
            #self._Encoders = ButtonMatrixElement(rows=[[self._Encoder0, self._Encoder1, self._Encoder2, self._Encoder3, self._Encoder4,  self._Encoder5, self._Encoder6, self._Encoder7]])
            #Device -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            #self.log_message("Device component set")
            #self._device = DeviceComponent(name='Device', is_enabled=False, layer=Layer(parameter_controls=self._Encoders), device_selection_follows_track_selection=True)
            #self._device.set_enabled(True)
            #self.set_device_component(self._device)