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

play_flag = 0
overdub_flag = 0

class FCB1010MXEF(ControlSurface):

    def __init__(self, *a, **k):
        super(FCB1010MXEF, self).__init__(*a, **k)
        self.show_message("-----------------------= FCB1010MXEF_v0.1 LOADING - maxcloutier13 says hi =----------------------------------------------------------")
        self.log_message("-----------------------= FCB1010MXEF_v0.1 LOADING - maxcloutier13 says hi =----------------------------------------------------------")
        with self.component_guard():
            #It's on
            self.log_message("-->It is on")
            #Alright ... so we got 10 buttons and 2 pedals to play with.
            #Buttons: CC22 to cc31 ... Pedal A: 64 - Pedal B: 65
            #Mirror the TriggerFinger functionality? ... We'll see!
            
            #self.log_message("TFMX Debug: Init first row")
            self._Pad0 = ButtonElement(True, MIDI_CC_TYPE, 14, 22, name='Pad0')        
            self._Pad1 = ButtonElement(True, MIDI_CC_TYPE, 14, 23, name='Pad1')
            self._Pad2 = ButtonElement(True, MIDI_CC_TYPE, 14, 24, name='Pad2')
            self._Pad3 = ButtonElement(True, MIDI_CC_TYPE, 14, 25, name='Pad3')           
            self._Pad4 = ButtonElement(True, MIDI_CC_TYPE, 14, 26, name='Pad4')            
            #self.log_message("TFMX Debug: Init second row")
            self._Pad5 = ButtonElement(True, MIDI_CC_TYPE, 14, 27, name='Pad5')            
            self._Pad6 = ButtonElement(True, MIDI_CC_TYPE, 14, 28, name='Pad6')
            self._Pad7 = ButtonElement(True, MIDI_CC_TYPE, 14, 29, name='Pad7')
            self._Pad8 = ButtonElement(True, MIDI_CC_TYPE, 14, 30, name='Pad8')
            self._Pad9 = ButtonElement(True, MIDI_CC_TYPE, 14, 31, name='Pad9')
            
            #Listeners on individual buttons
            #self.log_message("TFMX Debug: Listeners first row")
            self._Pad1.add_value_listener(self._trig_pad1, False)
            self._Pad0.add_value_listener(self._trig_pad0, False)
            self._Pad2.add_value_listener(self._trig_pad2, False)
            self._Pad3.add_value_listener(self._trig_pad3, False)
            self._Pad4.add_value_listener(self._trig_pad4, False)
            #self.log_message("TFMX Debug: Listeners second row")
            self._Pad5.add_value_listener(self._trig_pad5, False)
            self._Pad6.add_value_listener(self._trig_pad6, False)
            self._Pad7.add_value_listener(self._trig_pad7, False)
            self._Pad8.add_value_listener(self._trig_pad8, False)
            self._Pad9.add_value_listener(self._trig_pad9, False)
    
    # -- Button triggers ---------------------------------------------
    # Move left
    def _trig_pad0(self, value):        
        if value > 0:           
            self.log_message("TFMX Debug: Pad0 triggered")
    # Move right
    def _trig_pad1(self, value):        
        if value > 0:            
            self.log_message("TFMX Debug: Pad1 triggered")
    # Stop new
    def _trig_pad2(self, value):        
        if value > 0:           
            self.log_message("TFMX Debug: Pad2 triggered")
    # Record new       
    def _trig_pad3(self, value):        
        if value > 0:           
            self.log_message("TFMX Debug: Pad3 triggered")
    # Launch
    def _trig_pad4(self, value):        
        if value > 0:            
            self.log_message("TFMX Debug: Pad4 triggered")
    # Previous - to be defined in ableton
    def _trig_pad5(self, value):        
        if value > 0:
            self.log_message("TFMX Debug: Pad5 triggered")
    # Next - to be defined in ableton        
    def _trig_pad6(self, value):        
        if value > 0:
            self.log_message("TFMX Debug: Pad6 triggered")
    # Play/Pause
    def _trig_pad7(self, value):        
        if value > 0:
            self.log_message("TFMX Debug: Pad7 triggered")
    # Stop/Reset
    def _trig_pad8(self, value):        
        if value > 0:          
            self.log_message("TFMX Debug: Pad8 triggered")
    # Set New        
    def _trig_pad9(self, value):        
        if value > 0:            
            self.log_message("TFMX Debug: Pad9 triggered")
    
    # -- Functions ---------------------------------------------
    def _stop_reset(self):
        global play_flag
        if play_flag == 0:
            #Not playing, reset playing position to start
            self.song().stop_playing()
            play_flag = 1
        else:
            #Playing, stops, but tells play button to start from position next time
            self.song().stop_playing()
            play_flag = 2
        return
            
    def _play_pause(self):
        #Play/pause functionality
        global play_flag
        if self.song().is_playing == 0:
            #Song not playing
            if play_flag == 0:
                #Song is paused: unpause
                self.song().continue_playing()
            elif play_flag == 1:
                #Song is Stopped, play from selection start
                self.song().play_selection()
                play_flag = 0 
            else:
                #Song is stopped and reset, play from start
                self.song().start_playing()
                play_flag = 0  
        else:
            #Playing: pause
            self.song().stop_playing()
    
    def _move_clipslot(self, up):
        scene = self.song().view.selected_scene
        scenes = self.song().scenes
        max_scenes = len(scenes)
        for i in range(max_scenes):
            if scene == scenes[i]:
                #Found our guy
                if up == 1:
                    self.song().view.selected_scene = scenes[i-1]
                    self.show_message("TFMX Debug: Up!")
                else:
                    if scene == scenes[max_scenes-1]:
                        self.song().view.selected_scene = scenes[0]
                    else:
                        self.song().view.selected_scene = scenes[i+1]
                    self.show_message("TFMX Debug: Down!")
             
    def _move_track(self, left):
        #Get track and tracks
        track = self.song().view.selected_track
        tracks = self.get_all_tracks(only_visible = True)
        max_tracks = len(tracks)
        #Iterate to find current track's index.
        for i in range(max_tracks):
            if track == tracks[i]:
                #Found our track
                if left == 1:
                    self.song().view.selected_track = tracks[i-1]
                else:
                    if track == tracks[max_tracks-1]:
                        self.song().view.selected_track = tracks[0]
                    else:
                        self.song().view.selected_track = tracks[i+1]
                        
    def get_all_tracks(self, only_visible = False):
        tracks = []
        for track in self.song().tracks:
            if not only_visible or track.is_visible:
                tracks.append(track)
        #Include the master track?
        #NOPE tracks.append(self.song().master_track)
        return tracks
        
    def _launch_clip(self):       
        global overdub_flag
        #self.log_message("--> Track launch! -----")
        #self.song().view.highlighted_clip_slot.set_fire_button_state(True)
        _current_slot = self.song().view.highlighted_clip_slot 
        if _current_slot.is_playing == 0 and _current_slot.is_recording == 0:            
            self.song().view.highlighted_clip_slot.set_fire_button_state(True)
        elif _current_slot.is_playing == 1 and _current_slot.is_recording == 0:
            self.song().overdub = 1
            overdub_flag = 1
        elif _current_slot.is_playing == 1 and _current_slot.is_recording == 1 and overdub_flag == 1:
            self.song().overdub = 0
            overdub_flag = 0
        else:
            self.song().view.highlighted_clip_slot.set_fire_button_state(True)
    
    #Position on next valid clipslot    
    def _set_new(self):
        self.show_message("TFMX Debug: SetNew")
        #Find the first empty available clipslot and set it as highlighed
        self._find_empty_slot()
    
    #Stop clips then Position on next valid clipslot
    def _stop_new(self):
        self.show_message("TFMX Debug: StopNew")
        self.song().view.selected_track.stop_all_clips()
        #Position on first empty cell
        self._find_empty_slot()
        
    #Stop clips, position on next valid clipslot and fire record   
    def _record_new(self):
        self.show_message("TFMX Debug: RecordNew")
        self.song().view.selected_track.stop_all_clips()
        #Position on first empty cell
        self._find_empty_slot()
        self.song().view.highlighted_clip_slot.set_fire_button_state(True)
    
    #Find the first empty available clipslot and set it as highlighed
    def _find_empty_slot(self):        
        for clipslot in self.song().view.selected_track.clip_slots:
            if clipslot.has_clip == 0:
                self.song().view.highlighted_clip_slot = clipslot
                return
    