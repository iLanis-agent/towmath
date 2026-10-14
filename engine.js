// Tow math - trailer towing honesty.
// The tow rating on the ad is a best-case trim with a driver and nothing else.
// The sticker that runs out first is usually payload: tongue weight eats it.
// Verdicts judge the unrounded figure; rounding is for display only.
var TowMath = (function () {
  function pos(x) { return typeof x === "number" && isFinite(x) && x > 0; }
  function nneg(x) { return typeof x === "number" && isFinite(x) && x >= 0; }
  function r5(x) { return Math.round(x / 5) * 5; }

  // Labeled norm: honest tongue weight runs 10-15% of the loaded trailer.
  function tonguePlan(trailerLb) {
    if (!pos(trailerLb)) return { error: "the trailer weight must be above zero" };
    return { low: r5(trailerLb * 0.10), high: r5(trailerLb * 0.15) };
  }

  function renderTongue(r, trailerLb) {
    return "Your " + trailerLb + " lb trailer puts " + r.low + "-" + r.high
      + " lb on the hitch - the tongue weight the payload sticker will feel, before anyone climbs in.";
  }

  function payloadPlan(payload, people, cargo, tongue) {
    if (!pos(payload)) return { error: "the payload rating must be above zero" };
    if (!nneg(people) || !nneg(cargo) || !nneg(tongue)) return { error: "weights cannot go below zero" };
    var left = payload - people - cargo - tongue;
    return { left: Math.round(left), over: left < 0 };
  }

  function renderPayload(r, payload, people, cargo, tongue) {
    var s = "After " + people + " lb of people, " + cargo + " lb of cargo and " + tongue
      + " lb of tongue, your " + payload + " lb payload ";
    if (r.over) return s + "is over the sticker by " + Math.abs(r.left) + " lb - something gets left behind.";
    return s + "has " + r.left + " lb of margin.";
  }

  // Labeled norm: the common trailer-brake requirement line sits at 3,000 lb;
  // below 1,500 lb it rarely applies. Rules differ by state - check yours.
  function brakePlan(trailerLb) {
    if (!pos(trailerLb)) return { error: "the trailer weight must be above zero" };
    var verdict;
    if (trailerLb < 1500) verdict = "below the usual brake-law bite, but lights and the rating still apply";
    else if (trailerLb < 3000) verdict = "in the gray zone - some states already want brakes here";
    else verdict = "over the common 3,000 lb line - trailer brakes and a controller are the honest plan";
    return { verdict: verdict };
  }

  function renderBrake(r, trailerLb) {
    return "At " + trailerLb + " lb the trailer is " + r.verdict + ". Rules differ by state and speed - check yours.";
  }

  return {
    tonguePlan: tonguePlan, renderTongue: renderTongue,
    payloadPlan: payloadPlan, renderPayload: renderPayload,
    brakePlan: brakePlan, renderBrake: renderBrake
  };
})();
if (typeof module !== "undefined") module.exports = TowMath;
