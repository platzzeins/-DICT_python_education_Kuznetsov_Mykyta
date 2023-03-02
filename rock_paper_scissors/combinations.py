combinationsExtended = {
    "rock": ["scissors", "sponge", "wolf", "tree", "human", "snake", "fire"],
    "scissors": ["paper", "air", "sponge", "wolf", "tree", "human", "snake"],
    "paper": ["rock", "gun", "lightning", "devil", "dragon", "water", "air"],
    "fire": ["scissors", "snake", "human", "tree", "wolf", "sponge", "paper"],
    "snake": ["human", "tree", "wolf", "sponge", "paper", "air", "water"],
    "human": ["tree", "wolf", "sponge", "paper", "air", "water", "dragon"],
    "tree": ["wolf", "sponge", "paper", "air", "water", "dragon", "devil"],
    "wolf": ["sponge", "paper", "air", "water", "dragon", "devil", "lightning"],
    "sponge": ["paper", "air", "water", "dragon", "devil", "lightning", "gun"],
    "air": ["fire", "rock", "gun", "lightning", "devil", "dragon", "water"],
    "water": ["dragon", "devil", "lightning", "gun", "rock", "fire", "scissors"],
    "dragon": ["devil", "lightning", "gun", "rock", "fire", "scissors", "snake"],
    "devil": ["lightning", "gun", "rock", "fire", "scissors", "snake", "human"],
    "lightning": ["gun", "rock", "fire", "scissors", "snake", "human", "tree"],
    "gun": ["rock", "fire", "scissors", "snake", "human", "tree", "wolf"]
}

combinationsUsual = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock"
}
