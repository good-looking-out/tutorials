# How to Sidechain Audio in Ableton Live

Sidechaining uses the signal from one track to control how an effect responds on another track. A common example is placing a Compressor on a bass or chord track and using a kick drum as its trigger, so the target track reduces in level when the kick plays. Open [Ableton Live](https://www.ableton.com/en/live/) with an audible source track and a separate target track before following along.

## Video walkthrough

<div class="video-embed">
  <iframe
    src="https://www.youtube.com/embed/rbuTKgcteKo?rel=0"
    title="Learn Live: Sidechaining audio"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen>
  </iframe>
</div>

## Identify the source and target tracks

The **source** is the audio that triggers the effect, such as a kick drum, vocal, or percussion loop. The **target** is the track that contains the effect and changes in response, such as a bass, pad, background music, or an effect return.

For conventional ducking, insert **Compressor** on the target track. The source signal does not pass through the target track or become audible through it; it is used only by the Compressor’s detector. This means the source can stay routed to the Main track normally while it controls compression elsewhere.

Choose a source that has a clear rhythmic or level pattern. A clean kick track is a simple starting point. If the source is a full drum mix, use the detector EQ later in the process to focus on the part of that mix that should trigger the effect.

## Set up Compressor sidechain routing

1. Select the target track and add **Compressor** to its device chain.
2. Open Compressor’s sidechain section using the expand control in the device title bar.
3. Enable **Sidechain** in the external sidechain section.
4. In the sidechain source chooser, select the track that should trigger the Compressor.
5. Use the second chooser to select the available source point or Rack chain. For a Rack source, choose the individual chain if you need a specific sound, such as the kick inside a Drum Rack.

The source-point choices determine where the detector receives the signal. Pre-effects, post-effects, and post-mixer choices can produce different trigger levels, especially when the source has processing or automation. Start with the point that best represents the source you want the Compressor to detect, then change it only if the triggering is inconsistent.

Set Compressor’s sidechain **Dry/Wet** control to 100% when the external signal should be the only trigger. The **Gain** control raises or lowers the detector input without changing the source track’s audible mix level.

## Verify the sidechain signal before compressing

Use Compressor’s sidechain **Listen** control to monitor the detector input by itself. This helps confirm that the selected track, Rack chain, and source point are correct before changing threshold or timing. Disable Listen after checking, because it temporarily replaces the normal Compressor output with the detector signal.

Watch the sidechain input meter while the source plays. If it does not respond, first confirm that the source track is producing audio and that the selected Rack chain or source point is correct. If the meter responds but the effect is too weak, adjust the detector Gain or the Compressor controls rather than raising the source track’s mix volume.

## Create controlled ducking with Compressor

Start playback with both source and target audible, then lower the Compressor **Threshold** until the gain-reduction meter moves when the source plays. Lower thresholds cause more frequent or deeper compression. Increase the **Ratio** to make the level reduction more pronounced.

Set **Attack** to control how quickly the target begins to duck after the source arrives. Set **Release** to control how quickly it returns afterward. A very short release can create an obvious pulsing effect; a longer release can make the change less abrupt. Adjust these controls while listening to the full mix rather than to the target in isolation.

Avoid treating a large gain-reduction value as a goal by itself. The useful setting depends on the arrangement, source level, and desired result. Use enough reduction to make room for the source or create the intended rhythmic movement, then compare the result with Compressor bypassed.

## Shape the detector with sidechain EQ

Enable Compressor’s sidechain EQ when the detector should respond to only part of the source spectrum. For example, if a complete drum track triggers the Compressor but you want the kick to dominate the response, use a low-pass filter and adjust its frequency and Q until the detector emphasizes the kick’s low-frequency energy.

Use **Listen** while tuning the sidechain EQ to hear what the detector receives. This is often more reliable than guessing from the source track’s full sound. Once the detector is focused, disable Listen and make final Threshold, Ratio, Attack, and Release adjustments.

The sidechain EQ changes only the signal that triggers the Compressor. It does not EQ the source track in the mix or the target track’s audible output.

## Apply the same routing idea to other effects

Several Live effects can use an external sidechain signal. **Glue Compressor** supports a similar compression workflow. **Gate** can open a target only when the source crosses its threshold, which can create a tight rhythmic relationship between two parts. **Auto Filter** can use a sidechain input to move its filter with the source’s envelope.

The effect changes, but the routing principle remains the same: place the effect on the target, enable its sidechain controls, choose the source, and use the effect’s threshold, envelope, or timing parameters to set the response. Check each device’s documentation for its available sidechain controls rather than assuming they match Compressor exactly.

## Review the result in the full arrangement

Sidechaining is a mixing and arrangement tool, not only a special effect. Use it to create space for a kick, keep narration clear over music, or make a supporting part respond to a rhythmic source. Begin with one source-target pair and moderate settings, then listen across transitions and dense sections of the Set.

If the target disappears too long, shorten Release or reduce the compression amount. If the source does not create enough room, lower Threshold, increase Ratio, or refine the detector with sidechain EQ. Make the final decision with the full mix playing, because sidechain settings that sound exaggerated in solo can be appropriate in context.

For current details, see Ableton’s [Compressor sidechain parameters](https://www.ableton.com/en/live-manual/12/live-audio-effect-reference/), [Routing and I/O](https://www.ableton.com/en/live-manual/12/routing-and-i-o/), and [Sidechaining a third-party plug-in](https://help.ableton.com/hc/en-us/articles/209775325-Sidechaining-a-third-party-plug-in). The source walkthrough is Ableton’s [Learn Live: Sidechaining audio](https://www.youtube.com/watch?v=rbuTKgcteKo).
