"""Major Arcana — 22 trump cards, ids 1..22.

Field order: (card_id, name, rank/numeral, keywords, meaning, upright, reversed).
Ids follow the original Android convention where drawable ``card_01`` was
The Fool and ``card_22`` The World.
"""

# (id, name, numeral, keywords, meaning, upright, reversed)
MAJOR_ARCANA = [
    (1, "The Fool", "0",
     "Beginnings · Innocence · Spontaneity · Faith",
     "A fresh start taken on pure faith, stepping into the unknown with an open heart.",
     "The Fool heralds a genuine new beginning. Opportunities arrive without warning and the "
     "only requirement is the courage to say yes. Travel, leaps of faith and untried paths are "
     "favoured; the universe rewards your willingness to begin before every detail is certain.",
     "Reversed, The Fool warns of recklessness rather than trust. A step is being taken without "
     "preparation, or an old fear of leaping keeps you frozen at the cliff's edge. Consider which "
     "of the two applies, and either pause for planning or accept that no journey ever feels safe."),

    (2, "The Magician", "I",
     "Manifestation · Willpower · Skill · Resourcefulness",
     "The power to turn intention into reality through focused will and talent.",
     "Every tool you need is already on the table. The Magician appears when a desire is ready to "
     "be shaped into something concrete through clear speech, decisive action and concentrated "
     "effort. Speak your intention aloud and begin; the energy of creation flows through you now.",
     "The Magician reversed points to scattered energy, deception or unused talent. Someone may be "
     "manipulating a situation, or you are distracting yourself from the one action that matters. "
     "Realign your words with your truth before you commit."),

    (3, "The High Priestess", "II",
     "Intuition · Mystery · Inner voice · Secrets",
     "Deep intuitive knowledge that asks to be trusted rather than explained.",
     "The answer you seek is not in any outer voice but in the quiet beneath it. The High Priestess "
     "counsels stillness, listening and patience; dreams, coincidences and gut feelings carry real "
     "information now. Not everything needs to be revealed to be known.",
     "Reversed, she signals ignored intuition and secrets that corrode. You may be rationalising "
     "away what you already feel to be true, or withholding your inner knowledge from those who "
     "deserve it. Return to silence and let the inner voice re-establish itself."),

    (4, "The Empress", "III",
     "Abundance · Nurture · Creativity · Sensuality",
     "Fertile, creative energy that grows whatever receives patient care.",
     "The Empress is the great mother of the deck: abundance, comfort and creative fruit. Projects, "
     "relationships and even the body flourish under gentle, consistent attention. Say yes to "
     "pleasure, beauty and generosity — growth is your natural state right now.",
     "Reversed, The Empress warns of creative blockage or smothering care. Something is being "
     "overwatered and under-pruned, or your own needs have been left off the list. Tend to yourself "
     "first and growth will resume."),

    (5, "The Emperor", "IV",
     "Authority · Structure · Discipline · Stability",
     "Order imposed on chaos through disciplined leadership and clear boundaries.",
     "The Emperor brings structure, strategy and steady command. This is a moment for systems, "
     "rules and long-term plans rather than impulse. Authority is available to you — claim it "
     "calmly, set boundaries, and protect what you are building.",
     "Reversed, the Emperor shows rigid control, tyranny or an absent father-figure. Structure has "
     "become a cage, or authority is being exercised without wisdom. Loosen the grip and lead by "
     "service rather than force."),

    (6, "The Hierophant", "V",
     "Tradition · Teaching · Institutions · Belief",
     "Time-tested knowledge handed down through teachers, ritual and tradition.",
     "The Hierophant honours tradition, apprenticeship and the wisdom of institutions. Learning "
     "from a teacher, joining a community or following established practice will serve you now. "
     "Not every path needs to be invented; some have already been mapped.",
     "Reversed, he warns of dogma, rebellion for its own sake, or outgrown beliefs. An inherited "
     "rule no longer fits your truth. Question authority respectfully and write your own creed."),

    (7, "The Lovers", "VI",
     "Union · Choice · Harmony · Values",
     "A significant union or a heart-led choice between paths.",
     "The Lovers speak of deep connection — romantic or collaborative — and of the choices that "
     "define who we are. Alignment between your values and your actions brings harmony. When a "
     "choice appears, let the heart and the conscience decide together.",
     "Reversed, The Lovers indicate disharmony, avoidance of a necessary choice, or values out of "
     "alignment with behaviour. A relationship or commitment may need honest renegotiation before "
     "it can flourish again."),

    (8, "The Chariot", "VII",
     "Determination · Victory · Control · Direction",
     "Opposing forces harnessed to a single will, driving toward victory.",
     "The Chariot is momentum with a destination. Conflicting demands are reconciled through focus "
     "and discipline, and the road opens ahead of you. Take the reins, assert your direction and "
     "expect progress — hard-won, deliberate and public.",
     "Reversed, the Chariot veers. Aggression replaces drive, or too many destinations pull the "
     "reins apart. Slow the vehicle, choose one road, and remember that control begins with "
     "self-mastery."),

    (9, "Strength", "VIII",
     "Courage · Compassion · Patience · Inner power",
     "True strength as gentle courage that tames the wild without breaking it.",
     "Strength shows power expressed as patience, kindness and steady nerve. The lion is not "
     "defeated but befriended. Face the intimidating situation with a calm heart, and your gentleness "
     "will prove stronger than any force.",
     "Reversed, Strength flags self-doubt, raw impulse or courage spent on the wrong battle. The "
     "inner beast is driving instead of being guided. Breathe, forgive yourself, and reclaim the "
     "quiet authority you actually possess."),

    (10, "The Hermit", "IX",
     "Introspection · Solitude · Guidance · Wisdom",
     "Withdrawing to seek truth by one's own inner lamp.",
     "The Hermit calls for deliberate retreat from noise. Solitude, study and honest self-examination "
     "reveal what crowds have hidden. The answers belong to you alone for now; share them when the "
     "lamp has burned steady.",
     "Reversed, the Hermit warns of isolation that has outlived its purpose, or of hiding behind "
     "wisdom to avoid living. Come down from the mountain; the world and its lessons are waiting."),

    (11, "Wheel of Fortune", "X",
     "Cycles · Destiny · Turning point · Luck",
     "The great wheel turns and circumstances change with it.",
     "The Wheel turns in your favour. A cycle completes and a new one begins, often with surprising "
     "speed. Coincidences are meaningful; ride the momentum and stay flexible, because the highest "
     "point of the wheel is already in motion.",
     "Reversed, the Wheel resists. Bad timing, repeating patterns or luck running against the plan "
     "suggests fighting the current. Loosen your hold on outcomes; the wheel always turns again."),

    (12, "Justice", "XI",
     "Fairness · Truth · Law · Cause and effect",
     "Clear-eyed accountability: every effect traces honestly to its cause.",
     "Justice cuts through wishful thinking with clarity and fairness. Contracts, decisions and "
     "disputes resolve according to their true merit. Act with integrity and the judgement will "
     "land in your favour; the scales are weighing things exactly as they are.",
     "Reversed, Justice shows imbalance, bias or an avoided reckoning. Someone is not telling the "
     "whole truth — possibly you. An unfair outcome can still be corrected, but only by facing the "
     "facts without flinching."),

    (13, "The Hanged Man", "XII",
     "Surrender · New perspective · Pause · Sacrifice",
     "Deliberate suspension that transforms a problem by changing the viewpoint.",
     "The Hanged Man hangs willingly. Progress now comes through pausing, surrendering control and "
     "seeing the situation from an entirely new angle. What feels like stalling is actually deep "
     "preparation; the release you want follows the letting go.",
     "Reversed, he is stuck — sacrifice without meaning, or martyrdom performed for an audience. "
     "The pause has become avoidance. Either commit to the new perspective or step down and move."),

    (14, "Death", "XIII",
     "Transformation · Endings · Release · Rebirth",
     "An ending that clears the ground for an inevitable rebirth.",
     "Death rarely means literal death; it means transformation. Something — a role, a belief, a "
     "phase — has finished its work and must be released so the new can be born. Do not cling to "
     "the shed skin; what comes next cannot arrive while the door is barred.",
     "Reversed, Death resisted. An ending is being prolonged out of fear, draining energy that "
     "renewal needs. The transition will happen either way; choosing it willingly restores your "
     "power."),

    (15, "Temperance", "XIV",
     "Balance · Moderation · Alchemy · Patience",
     "Opposites blended with care into something wiser than either alone.",
     "Temperance is the art of blending. Extremes are tempered, conflicting needs find measure, and "
     "steady patient effort turns base metal to gold. Avoid excess in every direction; the middle "
     "path is not dull but precise.",
     "Reversed, Temperance signals excess, impatience or a life out of balance. One ingredient is "
     "overwhelming the mixture — work, pleasure, worry or indulgence. Re-measure the proportions "
     "and let time do its quiet work."),

    (16, "The Devil", "XV",
     "Bondage · Temptation · Shadow · Attachment",
     "The chains we choose: attachments and appetites that quietly rule from below.",
     "The Devil names the chain — a habit, a relationship, a fear — that pretends to be "
     "inescapable. The lock, however, opens from the inside. Look honestly at what binds you, "
     "especially what pleasure disguises, and the power of the bond will shrink on contact.",
     "Reversed, the chains are loosening. Awareness of the attachment is breaking its grip, though "
     "withdrawal is real. Freeing yourself now is slow, unglamorous and entirely possible."),

    (17, "The Tower", "XVI",
     "Upheaval · Revelation · Collapse · Awakening",
     "Sudden, necessary collapse of a false structure.",
     "The Tower strikes what was built on unstable ground. A shock, revelation or abrupt change "
     "topples assumptions, and the discomfort is proportional to how false the foundation was. Let "
     "it fall cleanly — what remains standing after the storm will be true.",
     "Reversed, the Tower trembles. Disaster is feared or barely deferred; change is resisted until "
     "it must arrive all at once. Dismantle the weak structure voluntarily while demolition is "
     "still a choice."),

    (18, "The Star", "XVII",
     "Hope · Renewal · Inspiration · Faith",
     "Serenity and renewed faith after the storm has passed.",
     "After the Tower, the Star. Healing water pours freely, inspiration returns, and a guiding "
     "light makes the long road feel walkable again. Hope is not naive here; it is accurate. Trust "
     "the quiet promise that you are being led somewhere kinder.",
     "Reversed, the Star dims. Discouragement, disconnection or lost faith has you looking down "
     "instead of up. The light has not left the sky — only your gaze has dropped. Small acts of "
     "self-care restore the sight."),

    (19, "The Moon", "XVIII",
     "Illusion · Dream · Anxiety · The unconscious",
     "Moonlit fog: not everything is what it appears to be, and feelings amplify.",
     "The Moon moves the reading into dream-logic. Fears magnify, facts blur, and intuition is "
     "needed precisely because the surface is unreliable. Do not force clarity at midnight; walk "
     "slowly, trust the deep currents, and wait for dawn to verify the shapes.",
     "Reversed, the fog lifts. Confusion releases, a deception is uncovered, and nightmares lose "
     "their grip. Truth that was obscured is emerging — let it arrive the rest of the way."),

    (20, "The Sun", "XIX",
     "Joy · Success · Vitality · Clarity",
     "Warm, open success — everything visible, everything alive.",
     "The Sun shines without subtlety: success, health, joy and simple truth. Achievements are seen "
     "and celebrated, relationships warm, and life feels briefly uncomplicated. Say yes to "
     "visibility; this is the card of being genuinely glad to be alive.",
     "Reversed, the Sun is veiled. Joy is present but dimmed by delay, false modesty or residual "
     "clouds. The success is real; only the celebration is postponed. Let yourself receive the "
     "warmth that is already yours."),

    (21, "Judgement", "XX",
     "Awakening · Reckoning · Calling · Renewal",
     "A summons to rise, account for the past and answer a higher calling.",
     "Judgement sounds the trumpet: an awakening, a calling, a moment of honest reckoning. The past "
     "returns not to punish but to be integrated. Forgive what must be forgiven, choose the higher "
     "path, and answer the call that has your true name on it.",
     "Reversed, the call goes unanswered. Self-judgement masquerades as conscience, or old "
     "regrets block the rising. The summons will repeat; meeting it sooner is the mercy."),

    (22, "The World", "XXI",
     "Completion · Wholeness · Achievement · Integration",
     "The circle closes: completion, travel, and the whole world in your hands.",
     "The World completes the great cycle. A significant chapter closes with mastery, integration "
     "and quiet triumph. Broad horizons open — literal travel, publishing, graduation, any finish "
     "line that becomes a gate. Dance once, then step through.",
     "Reversed, the World awaits its final stitch. A project is 95 percent complete but the last "
     "closure is avoided, keeping the next gate shut. Finish the unfinished; completion is a skill, "
     "not an accident."),
]
