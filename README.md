# EUW-Switch-Animation-Layers
This is a tool that makes switching between animation layers in Unreal Engine's sequencer easier by requiring a single button press. Useful for working with motion capture on metahumans as the sequencer can require lots of scrolling up and down to switch between animation layers. 

![Switch_Layers_UI](https://github.com/user-attachments/assets/548e5fb9-7fca-4b33-8da5-305ea8f72857)

Steps to use it:

Create an editor utility widget with two buttons. Name them animLayer and baseLayer.
![designer window](https://github.com/user-attachments/assets/40488dc6-5951-430a-bf93-ba60ff611cfb)

Create a section index int variable and bool variables for each of the buttons.
Recreate the node graph shown below and copy the provided code into the execute python script box.

![node graph](https://github.com/user-attachments/assets/5bd1fa2e-d34a-4f1a-8c4f-4ddf0a570e07)

In the content browser, right click on the EUW and hit "Run Editor Utility Widget".

![run EUW](https://github.com/user-attachments/assets/2960fd02-57cf-4005-8b4b-d583c460b76b)

In sequencer, make sure you have a rig selected and you should now be able to use the buttons to switch between animation layers.

![sequencer](https://github.com/user-attachments/assets/990a0bca-2c1a-4c9b-91b6-17e2d23dc2a7)
