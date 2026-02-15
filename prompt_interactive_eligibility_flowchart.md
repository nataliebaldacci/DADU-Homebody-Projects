# TASK: Make Eligibility Flowchart Interactive (Step-Through with YES/NO)

## The Problem

`dadu_eligibility_flowchart.html` was just rebuilt with the correct Nashville.gov eligibility order and 45+ external links. The content and links are correct. But it displays all steps at once as a static page. The user wants it to be **interactive**: each step appears one at a time, with YES/NO buttons that reveal the next step or show a result.

## What NOT to Change

- Do NOT change the step order (Land Use Table → Lot Area → Service District → Single Structure → Conditions → Special Cases)
- Do NOT remove any external links. Every link pill/button that exists now must remain.
- Do NOT change colors, fonts, or branding. Keep the current palette (var(--slate), var(--wheat), var(--eligible), var(--not-eligible), var(--conditional), etc.)
- Do NOT remove the shared header (homebody_header.js) or shared CSS (homebody_shared.css)
- Do NOT change the page's nav placement (RESOURCES > Learn > Eligibility Flowchart)

## What TO Change

Add JavaScript interactivity so the flowchart works as a step-through wizard:

### Behavior

1. **On page load:** Only Step 1 is visible. Steps 2-6 are hidden. A progress bar shows "Step 1 of 6".

2. **Each step has YES and NO buttons:**
   - **YES** → hides the current step's question area (but keeps it visible as a completed/collapsed summary), then reveals the next step with a smooth scroll-down animation
   - **NO** → shows a "Not Eligible" result card for that step with the reason, styled with var(--not-eligible) (#B58676) background. Include a "Start Over" button.

3. **Step 3 (Service District) is special** — it has 4 sub-options (USD, DADU Overlay, UDO, SP). Instead of a simple YES/NO, show 4 option buttons plus a "None of the above" button:
   - "I'm in the USD" → eligible by-right, proceed to Step 4
   - "I have a DADU Overlay (GSD)" → eligible with overlay, proceed to Step 4
   - "I'm in a UDO with DADU standards" → eligible, proceed to Step 4 with note to contact Planning
   - "I'm in an SP with DADU standards" → eligible, proceed to Step 4 with note to contact Planning
   - "None of the above" → Not Eligible result

4. **Step 5 (Zoning Conditions) is informational, not a gate.** After the user reaches Step 5, show the conditions checklist (size limits, height, setbacks, design, STR prohibition, owner occupancy) as reference cards, then a "Continue to Special Cases" button that reveals Step 6.

5. **Step 6 (Special Cases) is informational.** Show historic overlay and SP/UDO notes, then a final "ELIGIBLE" result card.

6. **Final result cards:**
   - **Eligible:** Green card (var(--eligible) #406A64 background, white text). Message: "Your property appears eligible for a DADU." Buttons: "View Property Report Card" → property-report-card.html, "Check Another Property" → resets flowchart
   - **Not Eligible:** Clay card (var(--not-eligible) #B58676 background, white text). Message varies by step. Button: "Start Over"
   - **Conditional:** Gray card (var(--conditional) #918A83 background, white text). For UDO/SP paths. Message: "Your property may be eligible pending Planning Department review." Button: "Contact Planning" (external link)

### UI Elements to Add

**Progress bar** at the top (below the hero):
```
Step 1 of 6: Land Use Table ●───○───○───○───○───○
```
- Filled circles for completed steps, hollow for upcoming
- Current step highlighted with var(--wheat)
- Completed steps are var(--eligible) green
- Bar background: var(--gray-light) #E2E2E0

**Completed step summary:** When a user clicks YES on Step 1, instead of completely hiding Step 1, collapse it into a small summary bar:
```
✓ Step 1: Land Use Table — Zoning permits DADUs    [Change Answer]
```
- Green left border (var(--eligible))
- Collapsed to ~50px height
- "Change Answer" link resets back to that step (and hides all subsequent steps)

**YES/NO buttons:**
```css
.btn-yes {
  background: var(--eligible);   /* #406A64 */
  color: white;
  padding: 12px 32px;
  border-radius: 8px;
  font-weight: 700;
  font-family: Inter, sans-serif;
  border: none;
  cursor: pointer;
}
.btn-no {
  background: var(--not-eligible);  /* #B58676 */
  color: white;
  padding: 12px 32px;
  border-radius: 8px;
  font-weight: 700;
  font-family: Inter, sans-serif;
  border: none;
  cursor: pointer;
}
.btn-yes:hover { opacity: 0.9; }
.btn-no:hover { opacity: 0.9; }
```

**"Show All Steps" toggle** in the hero or below the progress bar:
- Small link: "Prefer to read all steps at once? Show full flowchart"
- Clicking it reveals all steps simultaneously (static mode), hides YES/NO buttons
- Another click: "Return to interactive mode" — re-hides steps and resets

**"Start Over" button** on result cards and in the progress bar area:
```css
.btn-restart {
  background: var(--wheat);   /* #CBB279 */
  color: var(--slate);        /* #3A5566 */
  padding: 10px 24px;
  border-radius: 8px;
  font-weight: 700;
  border: none;
  cursor: pointer;
}
```

### Animation

- Steps reveal with a CSS transition: `max-height` from 0 to auto (or use `opacity` + `transform: translateY(10px)` fade-in)
- Smooth scroll to newly revealed step: `element.scrollIntoView({ behavior: 'smooth', block: 'start' })`
- Keep transitions under 300ms — snappy, not sluggish

### Quick Eligibility Checklist

The checklist section at the bottom of the page should remain visible at all times (not gated behind the interactive flow). It serves as a quick reference regardless of where the user is in the flow.

### Additional Resources Section

Also remains visible at all times at the bottom.

## Implementation Approach

The simplest approach: wrap each step's content in a `<div class="flow-step" id="step-N" style="display:none">` and use JavaScript to show/hide them. Add YES/NO buttons at the bottom of each step's content. The JS is straightforward — no framework needed, just vanilla JS event listeners.

Keep all the existing HTML content for each step. Just wrap it in the step containers and add the button rows.

## CONSTRAINTS

1. **All 45+ external links must remain functional and visible.** Do not hide links inside collapsed steps. When a step is collapsed after answering YES, the links for that step should still be accessible via the "Change Answer" expansion.
2. **No emoji.** Use SVG check marks or CSS-styled circles for the progress bar.
3. **No new colors.** Use only the existing CSS variables.
4. **Mobile responsive.** YES/NO buttons should stack vertically on small screens. Progress bar should wrap or simplify.
5. **Provide complete file contents** for `dadu_eligibility_flowchart.html`. Do not provide a partial diff.

## VERIFICATION

1. Page loads showing only Step 1 and progress bar
2. Clicking YES on Step 1 → Step 1 collapses to summary, Step 2 appears with smooth scroll
3. Clicking NO on any step → "Not Eligible" result card with correct explanation
4. Step 3 shows 5 option buttons (4 paths + "None of the above")
5. Step 5 shows conditions as reference, not as a gate
6. Final "Eligible" card appears after completing all steps
7. "Start Over" resets everything to Step 1
8. "Show All Steps" toggle works in both directions
9. "Change Answer" on collapsed steps resets from that point forward
10. All 45+ external links still present and clickable
11. Progress bar updates correctly at each step
12. Works on mobile (buttons stack, progress bar wraps)
13. Run link count verification:
    ```bash
    grep -oP 'href="[^"]*"' dadu_eligibility_flowchart.html | sort -u | wc -l
    ```
    Should be 45+ (same as before this change).

```bash
git add -A
git commit -m "Make eligibility flowchart interactive: step-through YES/NO wizard with progress bar"
git push origin main
```
