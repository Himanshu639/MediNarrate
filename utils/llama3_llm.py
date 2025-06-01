from langchain_groq import ChatGroq
import json
import os
from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(
    temperature = 0,
    groq_api_key = os.getenv('GROQ_API'),
    model_name = "llama-3.3-70b-versatile"
)

def generate_and_preprocess(text:str) -> dict:
    with open('utils/enhanced_prompt.txt', 'r') as file:
        prompt = file.read()

    full_prompt = prompt + text
    response = llm.invoke(full_prompt).content
    start = response.find('{')
    end = response.rfind('}') + 1

    json_obj = json.loads(response[start:end])
    return json_obj

if __name__ == "__main__":
    text = '''
        The Last Light of Ilyara

In a world where the sun itself was dying, there lay the ancient kingdom of Ilyara — a city of crystal towers and endless gardens, hidden in a valley the rest of the world had long forgotten. For centuries, the people of Ilyara lived beneath a sun that burned gold, then orange, then red. As the centuries passed, the crops grew thinner, the winters longer. Some said that even time itself had started to slow.

But Ilyara had a secret: the Lightkeepers.

A brotherhood — and sisterhood — sworn to preserve the last embers of magic left in the world. Deep beneath the palace, hidden behind silver doors, they guarded the Solstone: a crystal that shimmered with the stolen light of a thousand summer days.

Among the Lightkeepers was a girl named Lira. She was the youngest in a hundred generations — born with hair as pale as moonlight and eyes the color of stormy seas. It was said she could hear the crystal hum when others heard nothing. It was said she could feel the heartbeat of the world.

When the final winter came, and the sun shrank to a dying ember in the sky, the council called a meeting. The Solstone, they said, was weakening. Its light, once strong enough to fill a hundred cities, could now barely warm a single garden. Worse still, the wards that protected Ilyara were beginning to fail.

The enemy at their gates was not an army — it was the cold, endless night.

“We must take the Solstone and plant it beyond the valley,” said Elder Varyn, a woman whose face was lined like an old oak tree. “We must give it back to the world.”

“But to take it from here,” argued Master Renn, “would mean our end. Without the Stone, the city will freeze. We will all die.”

The council fell into shouting. Only Lira remained silent, feeling the hum of the Solstone vibrating through her bones. That night, unable to sleep, she wandered down into the secret chamber. She sat before the crystal, watching it pulse faintly like a dying star.

And it spoke to her.

Not in words, not in a language she could name, but in feeling — a deep, aching sadness, a memory of golden fields, a hunger to live.

Lira understood.

The Solstone wasnt meant to be hoarded. It was a seed — a seed meant to be planted.

At dawn, with the frost thick on the windows and the sky black as coal, Lira stole the Solstone.

She wrapped it in cloth spun from the first silkworms of Ilyara, cloth that could keep a secret from the very stars. She left through the broken gates and set out across the dead world. Ice cracked under her boots. Wind howled like wolves. She was just a girl, and the world was very old, and very tired.

But the Solstone burned against her chest like a tiny sun, and it guided her steps.

Days turned to weeks. Her breath froze on her eyelashes. She passed the ruins of cities — towers half-swallowed by sand, ships trapped in endless ice. She met no living creature save for a single white crow, which followed her, silent as a shadow.

At last, she came to the edge of the world.

It was not a place on any map — the ground fell away into a chasm that seemed to cut through the stars themselves. Wind roared up from the depths, carrying the scent of molten earth and ancient secrets. Here, the Solstone thrummed so loudly against her chest that she thought it might shatter her ribs.

She knelt at the edge.

And planted it.

Not with her hands, but with her heart. She pressed the Solstone into the ground, whispered the old words the elders had forgotten, and gave the last of her strength.

For a moment, there was nothing.

Then — the ground shook. Cracks split the stone. Light poured out in rivers, in waterfalls, in great blazing geysers. The sky split open. A new sun was born — small and fierce and blinding.

The world shuddered under its warmth.

Lira collapsed, smiling.

They say that if you go to the Valley of the New Sun, you can still find a girl with silver hair sitting among fields of gold. They say she is the first Lightkeeper and the last queen of Ilyara, though no one remembers the old names anymore.

They say she waits for the next soul brave enough to listen to the heartbeat of the world.

And to plant something new.
The Thousand Kingdoms of Aestra
Long before the stars were pinned into the heavens, before the oceans carved songs into the cliffs, there was only Aestra — the Great World. She was a land of endless skies, forests that breathed, and mountains whose roots touched the dreams of sleeping gods.

Aestra was alive.

Her rivers sang lullabies. Her stones whispered secrets. Her winds carried stories like seeds. And upon her skin, like ants on the back of a giant, lived the Thousand Kingdoms.

Each kingdom was a world in itself:

The Glass Cities of the western deserts, where towers rose like frozen lightning.

The Sapphire Reaches, a chain of floating islands drifting on rivers of sky.

The Endless Tundra, where beasts of silver fur howled beneath aurora-lit nights.

The Crimson Empire, where jungles choked the land and every leaf could cut like a blade.

And in the center of Aestra’s vast body, there stood the Worldspire — a tower so high it pierced the heavens and disappeared into the stars themselves.

Atop the Worldspire sat the Crown of Dawn, a relic said to grant its bearer dominion over all of Aestra. But it had lain untouched for eons, guarded by storms, dragons of living cloud, and riddles that twisted time itself.

The Prophecy
Legends spoke of the Convergence: a time when Aestra would shudder in her sleep and dream new dreams. In that moment, one soul — mortal or otherwise — could ascend the Worldspire and claim the Crown.

It would not be easy.

Every kingdom had its champions, its heroes, its kings and queens who would rise and fall in the struggle for the Crown.

But none expected the chosen soul to be a child — a girl from the broken village of Dunhollow, on the edge of the Bleeding Wastes.

Her name was Seren.

She was born under a black sun, during a storm that cracked mountains and turned rivers to steam. Her mother died giving birth. Her village believed she was cursed, and for years she lived as an outcast, speaking to the wind and listening to the stones.

Only the old smith, Master Vey, showed her kindness. He taught her how to listen — truly listen — to Aestra's heartbeat.

When Seren turned sixteen, the ground itself trembled. Mountains split. Seas drained. Stars fell like rain. It was the Convergence.

The race for the Crown had begun.

The Long Journey
Seren left Dunhollow with nothing but a blade of star-forged steel — a gift from Vey — and a map inked in blood and old sorrow.

Her journey took years. And in those years, she gathered companions, each broken in their own way:

Kael, the wingless prince of the Skyborne, who had been cast down for daring to love a mortal.

Mira, a sorceress from the Drowned Cities, with skin like sea-glass and a voice that could command tides.

Bran the Hollow, a knight whose body was a patchwork of old wars, bound by spells that barely kept his soul from slipping into death.

Together, they crossed the burning plains of Kharazad, where the sand itself was alive and hungry. They sailed the Starless Sea, where ghost-ships drifted and sirens sang from the dark. They climbed the steps of the Moonlit Sanctuaries, battling the Forgotten who clung to life only by hatred.

They faced traitors. They faced gods.
They faced themselves — their deepest fears, their buried guilt.

Each step forward cost them something precious.

The Betrayal
At the gates of the Worldspire, after all they had survived, they were betrayed.

Kael, desperate to reclaim his lost wings, struck a bargain with the Veiled King — a being of shattered dreams and hollow crowns. In exchange for the Crown, Kael would be made whole again.

He stole the Starblade from Seren and struck her down.

But Aestra herself intervened.

The earth cracked. The skies wept fire. The Worldspire opened, revealing not stairs, but a road made of memories — all the moments that had shaped Seren's life.

Bleeding, broken, but unbowed, Seren rose.

She forgave Kael even as he wept at her feet.

And alone, she walked the memory-road, higher and higher, until the stars themselves whispered her name.

The Crown
At the summit of the Worldspire, Seren found not a throne of gold, but a mirror.

In it, she saw every life she had touched. Every life she would touch. Every choice she had made. Every sorrow she had borne.

The Crown was not a thing to be worn.

It was a burden.

A promise.

Aestra did not need a ruler. She needed a guardian — someone who would walk with her, dream with her, and help her shape the new world to come.

Seren placed her hand on the mirror.

And the world was remade.

The Aftermath
Under Seren’s watch, the Thousand Kingdoms were no longer kingdoms at all. They became gardens, libraries, songs. People learned to speak with the trees again, to listen to the rivers, to dance with the wind.

Aestra healed.

And somewhere, far beyond the world’s edge, in a place where stars were born, Seren built a new tower — not to conquer, but to dream.

And the dreams she wove were made of hope.

And of light.

And they still fall from the sky like rain, for those with the heart to catch them.

🌟
    '''
    print(json.dumps(generate_and_preprocess(text),indent=4))
