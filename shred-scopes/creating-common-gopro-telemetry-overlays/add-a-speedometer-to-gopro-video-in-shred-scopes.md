# How to Add a Speedometer to GoPro Video in Shred Scopes

Shred Scopes can turn speed recorded in a compatible GoPro clip into an animated speedometer, numeric readout, bar, or gauge. The speed graphic can be exported separately for a video editor or rendered directly over the original footage with Source Composite.

This workflow requires usable GPS speed data in the active source.

## Before starting

Prepare:

- An original GoPro video containing GPS telemetry, or a saved extraction from that video
- A desktop computer and current browser
- A clip recorded with GPS enabled and a usable satellite lock
- A decision between miles per hour and kilometers per hour

An edited or recompressed copy may contain visible video but no telemetry. Use the original camera file whenever possible.

## 1. Load the GoPro source

Open [Shred Scopes](https://shredscopes.com/) on a desktop computer, sign in, and select "Studio" from the site navigation.

Choose one of these sources:

- "Choose Clip" for an original local GoPro file
- "Choose Metadata from Account" for previously saved telemetry

Wait until Studio finishes preparing the telemetry. Confirm that "Speed 2D (ground)" or "Speed 3D" is available before selecting a speed template.

## 2. Choose a speedometer template

At "Choose Template," select a built-in speed design. Available collections include speed gauges and text-oriented layouts in imperial and metric variants.

Examples include:

- Black Diamond Speed
- Flagship Speed or Flagship Speed Text
- Swell Speed or a Swell Speed Text layout
- Trailhead Speed or Trailhead Speed Text

Choose an imperial version for mph or a metric version for km/h. A template can also be customized after it opens, but starting with the correct unit variant reduces the number of changes required.

## 3. Choose ground speed or 3D speed

Speed templates commonly use "Speed 3D," which includes both horizontal and vertical movement. It can exceed ground speed during steep climbs, descents, or movement through the air.

Use:

- "Speed 2D (ground)" for motion across the Earth's surface without vertical movement
- "Speed 3D" for total movement through three-dimensional space

To change the stream in a customized template:

1. Select the speed-driven data-text, data-graphic, or data-ticks layer.
2. Open its data or input controls.
3. Choose "Stream."
4. Select the required speed stream.
5. Repeat the change for any other layer that displays or scales the same speed.

Keep the numeric readout, gauge, and tick marks mapped consistently. Mixing ground speed in the text with 3D speed in the needle can produce values that do not agree.

## 4. Set mph or km/h

Select the speed-driven layer and use "Convert" to choose the display unit.

Common options include:

- Miles per hour (mph)
- Kilometers per hour (km/h)
- Knots
- Minutes per kilometer
- Minutes per mile
- Feet per minute

For a conventional vehicle, cycling, skiing, or riding speedometer, mph or km/h is usually appropriate.

Change any static unit label so it matches the conversion. A numeric layer converted to mph should not retain a "km/h" text label.

## 5. Set the gauge range

A speedometer needs an input range suitable for the activity.

The main mapping choices are:

- "fit data min/max" to fit the recorded minimum and maximum to the graphic
- "fixed range" to use explicit limits, such as 0–30 mph or 0–100 km/h

An automatic range uses more of the gauge for a slow activity, but the same speed can appear at different positions across different clips. A fixed range keeps multiple exports visually comparable.

If an isolated GPS spike stretches the scale, enable "Clamp values" and set a reasonable maximum in the selected converted unit. Clamping affects the chosen layer input; it does not alter the extracted telemetry.

## 6. Preview the speedometer

Use "Play preview" and scrub the timeline to inspect:

- A stationary or low-speed section
- Normal travel speed
- The highest-speed section
- Acceleration and deceleration
- Frames with weak GPS coverage, if any

Confirm that the pointer, progress graphic, numeric value, tick labels, and unit label agree. Check that the speedometer does not exceed its visual range and remains readable over representative source frames.

## 7. Save a customized copy

Built-in templates are not overwritten. If the design was changed, open the "Template" menu and choose "Save As New" to keep a custom version.

Use a name that identifies the unit and range, such as an mph trail speedometer or a metric road speedometer.

## 8. Export the speed overlay

For a separate overlay, choose the output format in the Template Editor's export panel, select "Export," and keep the browser tab open and visible until rendering completes.

Use a transparency-capable MOV or WebM when the graphic will be placed over footage in another editor. A keyed-background MP4 requires a chroma-key effect during finishing.

For a finished video, select "Composite Mode," position the speedometer over the original video, and export the Source Composite result. Saved telemetry must be reconnected to the matching original source before Source Composite can use the video frames and audio.

## If speed is unavailable or incorrect

Check that:

- The original clip is loaded rather than an exported copy.
- GPS was enabled during recording.
- The camera had a usable satellite lock.
- The selected layer uses the intended speed stream.
- The numeric value, gauge, and ticks use the same conversion and range.
- A clamp or fixed range is not hiding valid high-speed values.

The completed template now displays GoPro speed in the intended unit and can be exported as a standalone graphic or a finished telemetry video.
