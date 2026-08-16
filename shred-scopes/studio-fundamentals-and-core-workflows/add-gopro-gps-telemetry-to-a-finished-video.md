# How to Add GoPro GPS Telemetry to a Finished Video in Shred Scopes

Shred Scopes can place GPS-driven graphics directly over the original GoPro footage and export the combined result as a finished MP4. This workflow is called Source Composite.

Use Source Composite when the video does not require a separate finishing workflow in another editor, or when a self-contained telemetry video is the required output.

## Requirements

Prepare the following:

- An original GoPro video containing the required GPS telemetry
- A desktop computer running a current Chromium-based browser
- A Shred Scopes account with full access
- Sufficient local storage for the exported MP4

Source Composite needs the original video because saved telemetry contains data but not the source frames or audio. GoPro `.360` footage cannot currently be previewed or rendered in Source Composite.

## 1. Load the GoPro source

Open [Shred Scopes](https://shredscopes.com/), sign in, and select "Studio" from the navigation.

Select "Choose Clip" and choose the original GoPro file. Wait for Studio to read the file and prepare its telemetry.

If telemetry was loaded from the account instead, select "Select Source Video" when prompted and choose the matching original GoPro clip. Studio validates the replacement before enabling Source Composite. A different clip can have incompatible timing, dimensions, GPS positions, or sampled values.

## 2. Choose a GPS telemetry template

Select a built-in or custom template using a GPS-derived stream. Common choices include:

- Ground or three-dimensional speed
- Altitude
- Distance traveled
- GPS course or heading
- GPS path
- Grade
- Vertical speed
- GPS-path acceleration

Use an imperial or metric variant that matches the required output. The template can be opened without changes or customized in the Template Editor before compositing.

Preview the timeline and confirm that the selected stream is present throughout the relevant part of the clip. A template cannot display a GPS value that was not recorded in the source.

## 3. Open Source Composite

Select "Composite Mode" in the top toolbar or press `M`.

The Source Compositor opens with the GoPro video behind the selected telemetry template. If "Composite Mode" is unavailable, confirm that:

- The source video has finished loading
- The original video is linked
- The source is not a `.360` file

The left control panel contains the canvas, source, template, timeline-range, compatibility, and encoding controls.

## 4. Set the output canvas

Choose an output size that matches the intended delivery format. Use a supplied canvas preset or select "Custom Size" to enter a specific width and height.

The source video can be fitted in two principal ways:

- "Cover" fills the output canvas and can crop parts of the source beyond its edges.
- "Contain" keeps the complete source visible and can leave unused canvas space.

Use the source "X," "Y," and "Scale" controls for precise placement. Rotation options of 0, 90, 180, and 270 degrees are available for footage that requires orientation correction.

Lock the source after its framing is correct to prevent accidental movement.

## 5. Position the telemetry overlay

Select the template overlay and place it where it remains legible without blocking important parts of the footage.

The template controls can be used to:

- Adjust X and Y position
- Change scale
- Align the template on the canvas
- Lock or unlock placement
- Duplicate the overlay
- Add another template
- Edit the selected template in a linked Template Editor tab
- Remove an added template from the composite

Adding more than one template makes it possible to combine, for example, a speed readout, GPS path, altitude value, and heading indicator in one video. Check the complete timeline because a position that works in one frame can cover a subject or become difficult to read later.

## 6. Set the export range

Drag the "In point" and "Out point" handles to select the portion of the GoPro video that should be exported. Drag the playhead or use preview playback to review the selected segment.

Enable "Rebuild data graphics from range" when the templates use cumulative values, automatic minimum-and-maximum ranges, elapsed time, or a range-relative GPS path. Rebuilding makes those graphics begin and scale according to the selected segment instead of the complete clip.

## 7. Choose the video settings

Select the Source Composite codec:

- H.264 provides the broadest MP4 playback and editing compatibility.
- HEVC/H.265 can reduce the bitrate required for similar quality, but browser encoder and playback support vary.

Set "Target Mbps" or leave its automatic setting enabled. The advanced controls include rate control, encoding priority, hardware preference, keyframe interval, source timecode, and resize sampling.

Use the "Compatibility" result to confirm that the browser can read the source, encode the selected settings, save the output, and continue while the tab remains visible.

## 8. Export the finished video

Select "Export" and choose a save destination. Keep the Studio tab open and visible until the render completes.

The exported MP4 contains:

- The framed GoPro video
- Every included telemetry overlay
- The original source audio
- The selected timeline range

Review the completed file before moving or deleting the source clip. If a change is needed, return to Source Composite, adjust the relevant source, template, range, or encoding control, and export a new file.

