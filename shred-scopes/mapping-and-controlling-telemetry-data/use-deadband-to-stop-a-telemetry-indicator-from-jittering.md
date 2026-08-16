# How to Use Deadband to Stop a Telemetry Indicator from Jittering

Deadband holds small numeric changes around a chosen center at that exact center. It is useful when sensor variation makes an indicator shake around rest, level, or another neutral value.

Values outside the deadband remain unchanged, and the extracted GoPro telemetry is not modified.

## Understand width and center

"Deadband center" sets the value to hold. "Deadband width" sets the total size of the window around it.

For example, a width of 0.10 centered on 0 holds values from −0.05 through 0.05 at exactly 0. Values below −0.05 or above 0.05 pass through unchanged.

The width extends across both sides of the center; it is not the distance from the center to each boundary.

## When to use deadband

Useful cases include:

- A vertical-speed pointer shaking around zero on level ground
- An acceleration or braking indicator moving during steady travel
- A lateral or longitudinal G dot wandering near its center
- A grade indicator changing sign around a nearly level section
- A signed data-text value rapidly alternating between small positive and negative numbers

Deadband is intended for a stable neutral zone, not for removing broad telemetry variation.

## 1. Open the data layer

Open [Shred Scopes](https://shredscopes.com/) on a desktop computer, sign in, select "Studio," and load the intended source.

Open the template and select the numeric data-text, data-graphic, or data-ticks layer that jitters. Expand "Input advanced."

Use "Template" > "Save As New" before retaining changes to a built-in design.

## 2. Choose the stream and unit first

Confirm "Stream" and select the final "Convert" setting.

Deadband uses the converted unit. A width entered after converting vertical speed to ft/min represents feet per minute. Changing to m/s later requires a new width.

## 3. Enable Deadband

Enable "Deadband," then enter:

- "Deadband center"
- "Deadband width"

For signed indicators, start with a center of zero. Choose a narrow width that contains only the unwanted neutral jitter.

For a nonzero neutral point, such as a value expected to rest around another baseline, set that baseline as the center and preview the complete range carefully.

## 4. Understand where deadband is applied

The relevant processing order is:

1. Unit conversion
2. Input clamping
3. Deadband
4. Range mapping

If a value is first clamped into the deadband window, it is then held at the center. The mapped graphic receives the deadband result.

Deadband settings affect only the selected layer input.

## 5. Compare deadband with smoothing

Deadband and smoothing solve different problems:

- Deadband snaps every value inside a defined window to one center value.
- Smoothing averages changes over time to reduce rapid motion.

Use deadband for a stable neutral state. Use smoothing when the complete movement needs to become less abrupt.

They can be combined, but heavy smoothing plus a wide deadband can remove genuine small events. Add one control at a time and preview the result.

## 6. Compare deadband with clamping

Clamping imposes outer minimum and maximum limits. Deadband stabilizes an interior window.

A signed gauge can use:

- Outer clamps to prevent impossible visual travel
- A small deadband around zero to stop neutral jitter
- A symmetric range to keep zero centered

Each control serves a separate role.

## 7. Preview the boundary behavior

Scrub through:

- Values well inside the deadband
- Values close to each boundary
- A slow departure from neutral
- A fast event crossing the window
- A return to neutral

Confirm that meaningful small movement begins at an appropriate point. If the indicator stays neutral too long, reduce the width.

Check data text as well as graphics. A pointer can appear stable while an unclamped or deadband-free numeric layer continues to flicker.

## 8. Apply consistent settings where needed

When text and a graphic should agree, give both layers the same stream, conversion, center, and width.

Different deadband settings can be intentional. For example, text may show fine detail while a pointer remains stable. Make that distinction clear through the design rather than leaving the layers apparently inconsistent.

## 9. Know the limitations

Deadband applies to numeric streams. It does not alter GPS Path or GPS Time.

It also does not correct:

- Missing telemetry samples
- Incorrect GPS positions
- A poorly chosen camera-axis stream
- An unsuitable range or direction
- Jitter far outside the selected window

Select the correct stream and unit before treating the issue as neutral noise.

## 10. Save the stable indicator

Save the custom template after checking the full timeline and both deadband boundaries.

The selected indicator now remains fixed at its intended neutral center during small fluctuations while preserving larger telemetry changes outside the window.
