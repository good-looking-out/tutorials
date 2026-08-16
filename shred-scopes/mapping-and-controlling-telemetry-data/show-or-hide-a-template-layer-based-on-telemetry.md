# How to Show or Hide a Template Layer Based on Telemetry

Data-driven visibility allows a template layer to appear only while a selected input is inside an optional minimum and maximum range. This can show an "In Air" message during detected airtime, reveal a warning above a speed threshold, or display a braking indicator only for negative longitudinal G.

Visibility conditions affect rendering at each frame. They do not delete the layer or change the source telemetry.

## Distinguish conditional and manual visibility

The eye control in the layer list manually shows or hides a layer for the complete template.

"Visible when" is different. It evaluates telemetry as the timeline moves and changes whether the layer is rendered at each frame.

The layer must remain manually visible for its telemetry condition to have a visible result.

## 1. Open a data-driven layer

Open [Shred Scopes](https://shredscopes.com/) on a desktop computer, sign in, select "Studio," and load the intended telemetry.

Open a template and select the data-text, data-graphic, or data-ticks layer whose visibility should change. Expand its data or input controls.

Create a custom copy before changing a built-in template.

## 2. Choose the controlling stream

Select the stream that should both drive or control the layer. For a multi-input graphic, use the "Input" setting under the visibility controls to choose which of its mapped inputs determines visibility.

Set the final unit conversion before entering thresholds. A speed condition entered after conversion to mph should use mph values.

## 3. Enable Visible when

Enable "Visible when," then configure an optional minimum, maximum, or both.

The layer appears while the controlling value remains inside the allowed range.

Examples include:

- Set a minimum above the inactive value for an "In air" stream so an "In Air" label appears during detected events.
- Set a minimum speed for a high-speed marker.
- Set a negative maximum for a braking indicator driven by longitudinal G.
- Set both limits for a label that should appear only inside one operating band.

Leave an unnecessary boundary unset rather than entering an arbitrary extreme.

## 4. Add hysteresis near a threshold

If the value repeatedly crosses a threshold, the layer can flicker on and off. "Hysteresis" adds a buffer around the boundary so a small reversal does not immediately switch the state again.

Use it for:

- Speed hovering around a warning threshold
- G-force fluctuating around a trigger value
- Grade changing near level
- A binary-like event with noisy boundaries

Start with a small buffer in the selected unit and preview both directions across the threshold.

## 5. Require the condition to persist

"Hold frames" requires a changed condition to remain present for the entered number of frames before the visibility state switches.

This can reject one-frame threshold crossings. It can also delay the appearance or disappearance of the layer, so keep the value short enough for the intended event.

For brief events such as airtime, a large hold can hide the event completely or keep the label visible after it ends.

## 6. Build a high-speed warning

1. Add data text containing the warning or create a data graphic.
2. Map it to the chosen speed stream.
3. Convert to mph or km/h.
4. Enable "Visible when."
5. Set the minimum warning speed.
6. Add modest hysteresis if the source hovers near the boundary.
7. Add a short hold only if isolated frames cause flicker.
8. Preview accelerations and decelerations through the threshold.

The threshold, text unit, and any adjacent speedometer should use the same conversion.

## 7. Build an in-air label

1. Add a data-text layer.
2. Map it to "In air."
3. Use a text map to display "In Air" for the active value.
4. Enable "Visible when."
5. Set a minimum that excludes the inactive value and includes the active value.
6. Preview frames before takeoff, during the detected event, and after landing.

The source must contain the in-air stream. The condition does not detect jumps from visible video.

## 8. Test both boundaries

Scrub through values:

- Clearly outside the condition
- Just below each threshold
- Exactly around each threshold
- Just inside the condition
- Clearly inside it

Play the preview at normal speed to judge flicker and delay. Frame-by-frame inspection alone may not reveal whether a hold feels too long.

## 9. Coordinate related layers

If a warning consists of text, icon, and background, apply matching conditions to each layer or group the design after verifying its behavior.

Separate conditions can become inconsistent if thresholds, conversions, hysteresis, or hold values differ. Review every layer participating in the conditional component.

Use a text map instead of visibility when only the wording should change and the layer should remain present.

## 10. Save the conditional template

Save the custom template after testing the complete timeline and every threshold direction.

The selected layer now appears only under the intended telemetry condition, with hysteresis and hold behavior controlling unwanted flicker.
