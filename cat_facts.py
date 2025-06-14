import random

cat_facts = [
    "Cats have five toes on their front paws, but only four on the back.",
    "A cat can jump up to six times its length.",
    "Cats have 230 bones in their bodies, while humans only have 206.",
    "The average cat sleeps 13 to 16 hours a day.",
    "Cats have a strong territorial instinct.",
    "Most cats dislike water because their fur doesn't insulate well when it's wet.",
    "A cat’s whiskers are generally about the same width as its body.",
    "Isaac Newton is believed to have invented the cat door.",
    "Some cats are allergic to humans.",
    "The oldest cat ever recorded lived to be 38 years old.",
    "Cats sweat through their paws.",
    "Male cats are more likely to be left-pawed; females are usually right-pawed.",
    "Cats can run at speeds up to 30 mph.",
    "Cats have a third eyelid called a haw.",
    "A group of kittens is called a kindle.",
    "The average house cat can reach speeds of up to 30 mph.",
    "Cats' purring may help heal bones and reduce pain.",
    "Cats have 32 muscles in each ear.",
    "A cat's brain is 90 percent similar to a human's.",
    "The world's richest cat inherited $13 million from its owner.",
    "Some cats chirp or chatter when watching birds.",
    "Cats can make over 100 different vocal sounds.",
    "Calico cats are almost always female.",
    "Black cats are considered good luck in Japan.",
    "In Ancient Egypt, killing a cat was punishable by death.",
    "Cats have been domesticated for nearly 9,000 years.",
    "Cats can drink seawater to survive.",
    "The heaviest domestic cat on record weighed over 46 pounds.",
    "The smallest cat breed is the Singapura.",
    "Cats don't have a sweet tooth.",
    "When cats grimace, they're usually using the Flehmen response to analyze scents.",
    "Most cats hate citrus scents.",
    "Cats use their tails for balance.",
    "Your cat recognizes your voice but may choose to ignore you.",
    "A cat’s heart beats nearly twice as fast as a human’s.",
    "Whiskers are deeply embedded and connected to the nervous system.",
    "Cats can see in near total darkness.",
    "The average cat’s hearing is better than a dog’s.",
    "Cats mark you as their territory by rubbing against you.",
    "A cat's purr vibrates at a frequency of 25 to 150 Hertz.",
    "Cats were often mummified in Ancient Egypt.",
    "Cats groom each other to show affection and as a social behavior.",
    "Cats can dream during REM sleep, just like humans.",
    "Some cats enjoy playing fetch.",
    "Polydactyl cats have more than the usual number of toes.",
    "The Maine Coon is the largest domesticated cat breed.",
    "Cats rarely meow at each other — meowing is mostly for communicating with humans.",
    "Kittens develop their sense of smell at about 3 weeks old.",
    "White cats with blue eyes are often deaf.",
    "Cats can rotate their ears independently 180 degrees.",
    "A cat’s tongue is covered in tiny, backward-facing barbs.",
    "Cats have a special reflective layer in their eyes called the tapetum lucidum.",
    "Some cats headbutt to mark you with their scent glands.",
    "A cat’s nose is as unique as a human fingerprint.",
    "Kneading is a leftover behavior from kittenhood.",
    "Tortoiseshell cats are almost always female.",
    "Cats can get sunburned, especially those with white fur.",
    "Each cat's meow is unique to its personality.",
    "Feral cats are not socialized to humans and are often not adoptable.",
    "Kittens open their eyes between 7–14 days after birth.",
    "Indoor cats generally live longer than outdoor cats.",
    "Cats can’t see directly under their noses.",
    "Some cats are lactose intolerant.",
    "Cats walk like camels and giraffes — both right feet first, then both left.",
    "Cats have scent glands in their paws.",
    "The first cloned cat was named CC, short for Carbon Copy.",
    "Cats use body language more than vocal communication.",
    "Cats can recognize their name, even if they ignore it.",
    "When a cat shows you its belly, it may not mean it wants to be petted there.",
    "The Jacobson’s organ helps cats detect pheromones.",
    "Male cats are called toms; females are called queens.",
    "A cat can survive a fall from a high-rise building due to their “righting reflex.”",
    "Cats dream about their day just like humans.",
    "The world’s longest cat was over 48 inches long.",
    "The Turkish Van cat is known for loving water.",
    "Cats can detect ultrasonic sounds made by rodents.",
    "Purring can be a sign of pain as well as contentment.",
    "In the Middle Ages, cats were associated with witches.",
    "Some cats suffer from feline acne.",
    "Kittens start purring at just a few days old.",
    "Some breeds, like the Bengal, are known for their dog-like behavior.",
    "Cats can remember people and places for years.",
    "The average cat lives 12–16 years, but some live over 20.",
    "A cat’s tail contains about 10percent of the bones in its body.",
    "Cats can develop separation anxiety.",
    "Many cats love cardboard boxes because they feel secure in them.",
    "Cats' spines are extremely flexible.",
    "A cat's hearing range is 48 Hz to 85 kHz — humans top out at 20 kHz.",
    "There are over 70 recognized cat breeds.",
    "Cats sweat through the pads on their paws.",
    "Cats use their tails to communicate emotions.",
    "Some cats grow a thick undercoat in winter and shed it in spring.",
    "Cats bury their waste to hide their scent from predators.",
    "A cat can squeeze through an opening the size of its head.",
    "Some cats trill as a sign of happiness.",
    "Grooming is a bonding activity between cats.",
    "Cats can smell with their mouths using the vomeronasal organ.",
    "The average domestic cat weighs around 8–10 pounds.",
    "Cats have binocular vision up to 20 feet.",
    "Many cats instinctively chase laser pointers because of their prey drive.",
    "Cats can be trained with clickers and treats.",
    "Your cat may bring you “gifts” to share their hunting success.",
    "Some cats enjoy watching TV or YouTube videos of birds and mice."
]


def get_random_cat_fact():
    return random.choice(cat_facts)
