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
            #Alright ... so we got 10 buttons and 2 pedals to play with.
            #Buttons: CC22 to cc31 ... Pedal A: 64 - Pedal B: 65
            #Mirror the TriggerFinger functionality?
            
            #Bottom row
            self._Pad0 = ButtonElement(True, MIDI_CC_TYPE, 15, 22, name='Pad0')        
            self._Pad1 = ButtonElement(True, MIDI_CC_TYPE, 15, 23, name='Pad1')
            self._Pad2 = ButtonElement(True, MIDI_CC_TYPE, 15, 24, name='Pad2')
            self._Pad3 = ButtonElement(True, MIDI_CC_TYPE, 15, 25, name='Pad3')           
            self._Pad4 = ButtonElement(True, MIDI_CC_TYPE, 15, 26, name='Pad4')
            #Top row
            self._Pad5 = ButtonElement(True, MIDI_CC_TYPE, 15, 27, name='Pad5')            
            self._Pad6 = ButtonElement(True, MIDI_CC_TYPE, 15, 28, name='Pad6')
            self._Pad7 = ButtonElement(True, MIDI_CC_TYPE, 15, 29, name='Pad7')
            self._Pad8 = ButtonElement(True, MIDI_CC_TYPE, 15, 30, name='Pad8')
            self._Pad9 = ButtonElement(True, MIDI_CC_TYPE, 15, 31, name='Pad9')
            
            #Listeners on individual buttons
            self._Pad0.add_value_listener(self._trig_pad0, False)
            self._Pad1.add_value_listener(self._trig_pad1, False)
            self._Pad2.add_value_listener(self._trig_pad2, False)
            self._Pad3.add_value_listener(self._trig_pad3, False)
            self._Pad4.add_value_listener(self._trig_pad4, False)
            
            self._Pad5.add_value_listener(self._trig_pad5, False)
            self._Pad6.add_value_listener(self._trig_pad6, False)
            self._Pad7.add_value_listener(self._trig_pad7, False)
            self._Pad8.add_value_listener(self._trig_pad8, False)
            self._Pad9.add_value_listener(self._trig_pad9, False)
            
    def _trig_pad0(self, value):        
        if value > 0:
            self.show_message("TFMX Debug: Pad0 triggered")
    
    def _trig_pad1(self, value):        
        if value > 0:
            self.show_message("TFMX Debug: Pad1 triggered")
    
    def _trig_pad2(self, value):        
        if value > 0:
            self.show_message("TFMX Debug: Pad2 triggered")
            
    def _trig_pad3(self, value):        
        if value > 0:
            self.show_message("TFMX Debug: Pad3 triggered")
    
    def _trig_pad4(self, value):        
        if value > 0:
            self.show_message("TFMX Debug: Pad4 triggered")
    
    def _trig_pad5(self, value):        
        if value > 0:
            self.show_message("TFMX Debug: Pad5 triggered")
            
    def _trig_pad6(self, value):        
        if value > 0:
            self.show_message("TFMX Debug: Pad6 triggered")
    
    def _trig_pad7(self, value):        
        if value > 0:
            self.show_message("TFMX Debug: Pad7 triggered")
    
    def _trig_pad8(self, value):        
        if value > 0:
            self.show_message("TFMX Debug: Pad8 triggered")
            
    def _trig_pad9(self, value):        
        if value > 0:
            self.show_message("TFMX Debug: Pad9 triggered")
    