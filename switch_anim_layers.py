# Script by Cameron Detig 02/2024
# Used as part of an Editor Utility Widget in Unreal Engine.
# Makes switching between animation layers in sequencer easier by making it a single button.
# Particularly useful for rigs with lots of controls, like metahumans.

import unreal

print("Running switch anim layers script")


def is_control_selected():

    #Get all rigs in level sequence
    lvl_seq = unreal.LevelSequenceEditorBlueprintLibrary.get_current_level_sequence()
    rig_prxs = unreal.ControlRigSequencerLibrary.get_control_rigs(lvl_seq)
    active_rig = []

    #Iterate through control selection to find the rig the selection belongs to...
    for i in range(len(rig_prxs)):
        rig = rig_prxs[i].control_rig
        #Query selected control in Sequencer
        sel_ctrl = rig.current_control_selection()

        if len(sel_ctrl) > 0:
            #set the selected_control variable to the selected controls
            selected_controls = sel_ctrl
            active_rig.append(rig_prxs[i])
            #control is found so exit the loop
            break;
        else:
            print('No rig found')
            
    #This will error if no control is selected and switch to searching for tracks.
    print("selected controls:")
    print(selected_controls)

    selected_rig = active_rig[0].control_rig
    print("selected rig:")
    print(selected_rig)

    selected_track = active_rig[0].track
    print("selected track:")
    print(selected_track)

    sections = selected_track.get_sections()
    print("track sections:")
    print(sections)

    #clear selection
    selected_rig.clear_control_selection()

    #Use the section_index variable passed to the script to select 
    #the section we are switching to. Reselect the control with the correct
    #section active.
    selected_track.set_section_to_key(sections[section_index])
    for i in range(len(selected_controls)):
        selected_rig.select_control(selected_controls[i])
    
    
def is_track_selected():
    #get selected track. will error and end function if no track is selected.
    selectedTrack = unreal.LevelSequenceEditorBlueprintLibrary.get_selected_tracks()[0]

    #make an array of the sections of the control rig
    sections = selectedTrack.get_sections()
    print(sections)
    
    #Use the section_index variable passed to the script to select 
    #the section we are switching to.
    selectedTrack.set_section_to_key(sections[section_index])
            
            
def is_binding_selected():
    #get the selected object
    selected_bindings = unreal.LevelSequenceEditorBlueprintLibrary.get_selected_bindings()
    #print(selected_bindings[0].get_display_name())
    #print(selected_bindings[0].get_tracks())
    
    #find the control rig track
    controlRigTrack = selected_bindings[0].find_tracks_by_type(unreal.MovieSceneControlRigParameterTrack)
    print(controlRigTrack)
    
    #make an array of the sections of the control rig
    sections = controlRigTrack[0].get_sections()
    
    #Use the section_index variable passed to the script to select 
    #the section we are switching to.
    controlRigTrack[0].set_section_to_key(sections[section_index])
    
    
#Search for what is selected in sequencer and attempt to switch the active section.
try:
    is_control_selected()
except:
    print("no control is selected, looking for section...")
    try:
        is_track_selected()
    except:
        print("no track is selected, looking for binding...")
        try:
            is_binding_selected()
        except:
            print("no binding is selected, exiting script.")



print("End of switch anim layer script")
