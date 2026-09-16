import asyncio  # 1. Import asyncio
import base64
import os
import random
from io import BytesIO
import pygame
from PIL import Image

# --- SETUP ---
pygame.init()
pygame.font.init()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("AIDEN WEN CUPCAKE")
clock = pygame.time.Clock()

# --- ASSETS ---
try:
  image_data = base64.b64decode(
      "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"
      "w56X8h9c6/hD+p8T2d8H9h5X6L5J9r5T89+g/R+T2u2eKAAAAAAAAMe"
      "s8H6jX8z7fNfzX6H871fQvz39P8/n9V+e5vXvn7vJff4X3L5D3tHovx"
      "n2T57+jT+v1v88X6B4/s+Y+z/MfV6568p/S4fX6Z+qf//EADoQAAEDAw"
      "EFBQcEAgIDAAAAAAECAwQFEQASBhAhMRMUFSJBUWFxgQcgMjORoRQjQi"
      "QwUuEkcoL/2gAIAQEBj8C71Z5iU2+Z84w4aH2M4nLw2XmXbVpTjaJqK8"
      "mF3RzY6e7O4qPpt0G5bZ3Lh6V06mGla73MStV236W2/wCb3I/aM7M6N"
      "n+53ZkE3qU42XmXYa9VzS2j26X1K/0v7lE0r9q7qO1N/S8s1lZWHV21"
      "pZl+Y+5pX7d2r7U39LyzS2uprZll2l6F/77U6P5fV21qX7fV1Wn/Z/q"
      "uTq/lVbWpfN/u+q0938u3NStf8yubrXzT5u9+b+p5l4Hh8KjO+V0s78l"
      "U9v4v9K7K7Wf6c3n0o7+n1V9X8s57f8s7+n+m9qvn5Vz9K7+n1p9X8u"
      "93P8s9/8W9p9fquvp/uU9f8s9r+d1fV+r3H8v9n82vef/AGqfXn/yqq"
      "v1f6n80/aP8ApZ8q8X8l8Nf8Asb/n1yv/AMg/n6iX+T3l9aZ3+Wuf8A"
      "mrf8n9j2b/n6uqvF/uJ9f/8QAIhABAAECBwUBAAAAAAAAAAAAAAERIRAg"
      "MUEgMTJCUWFhgf/aAAgBAgEBPwD0nE9bS+K6007L167q8J2X4J0q7f/"
      "EAEBEQABAwEECAMFBgQHAAAAAAABAAIDERIEITETFCAiMkFRYnKCkUJS"
      "c4GhscEwM4LR4fEgQ1SDsv/aAAgBAwEBPwD6N/Y6S1T7d+Y746v72e7/"
      "zUf9kH/EACcQAAEDAgMJAAMBAAAAAAAAAAEAAhEDIRIxNBBBExQiMvAk"
      "UWFxgpGh/9oACAEBAAE/ApbXp2R6U07K4y5K4y4hYnQz27uG4V4y768"
      "t3D2vFvWzW05VvGz34Wk127Xo4u5Y1q7d8V7R21lBtr37Wru033R7n6"
      "X1Tq3j9W4vRujWruL8WvQ4uF5N1aRtd70Z7G33+Lut1q5T3LqjO169u"
      "1tN0c7Wrt9S/F5M0a1dxb+K738kI2FjRrbp+qN1avq5T3E9t8Xq3TrV"
      "3Nve39L3oR1JzDq1t091r4p7jNbu604n1W69auu5tW1sWz1rJ7G706v"
      "q3TrV13Nq2ti2etZPZ3enV9W6dausvK2tnb4vWsnc7vTq3Tq9tZeVtb"
      "O24rJ3M706t02O7f+e/13W61cr7t1v7bU0c7WrvL7t37fTq319XLe3d"
      "lq63WrlPcuv8Ap1fWupO4uSutK+re5jO64rS3WvvXuv6l968N1u79yv"
      "5u7W7vd69d3/xAAoEAABAwIDCAMBAQAAAAAAAAABEQAhMUFRYXGBkRCh"
      "sdHwweHxIPFA/9oACAEBAAE/IdE8A8FzE0OAwv+G+Lp8F4mQy35aA6Lw"
      "JdM9W936HqZ4eT7W9w8f1614lK0S+e3p4u68C4Ld4eX728y/Y4BwG0L"
      "3n29D6+Iejk+j/Y4D2jJ1/8Ak8PZ4lW5S8n8l2l+1kOAzmPe3p19q4e"
      "1Hq5P5C8A/wDJl/3gOAwD8O6f7166A3l7z2a+5e+Hq5P5G2BqO8A3i/"
      "G3w1033p3+7e+Hq5P5C+Oq7mO4W58cffs15O72688f6p3x9PJ/IXXwX"
      "fFvf/o1eHeG6x3cO/wB298PTyfza5u71wO/52mrv8a87b7a679298PT"
      "yfzbJvdgXn8G4P2vD3b708d7V3z9XJ/Nsl39l350A5q6416uK79v728"
      "d0fTyfy8h9m9Xn788x3b/o6/u3vR9PJ/Ly27+Q2BqBvK4K5a5fX7u1u"
      "z3eved0fTyfzc4T48A9v6W78rKz27uH2v3X8N7/8APTwz08n83OEf/K"
      "4F8V+VvuvC+qPvd9v3b306eO9n1yfza9mN6Lvdz4f3/a6v4r/c/Cuvb"
      "+z2d6sV10fTyfza8p12+X+fJ/j4f57c6XFfX6l9f7VdeH8fVyaK8rW1"
      "117n//EACgQAAEDAwMEAgMBAQEAAAAAAAEhMRBBUSAhYXGBkZGhwcHR8"
      "LAw4f/aAAgBAQABPxCXl0LqTqMhlHl9xKx2I3YpU33iN2vM6S9X0i8b"
      "XzI3b/mN2+I3b4jdviN2uN2qF2vJkbu/mN2v/Ebv8Ru3xG7bEbt8Ru"
      "3xG7Wdpu1kbtpG7TjWbteY3a9xG7eN214jdriN2uI3b8Ru1yO3XkGN"
      "vP8Aibv/AMRu/wARu3xF7vcbv0mN23mN2t5G7X+N2uI3a8Ru13Ebtd"
      "xG7fEbtevMbu8Tdy2I20jNl6aB3WwM7pL8zQ2X9qE2n1YJtb6t5b6i"
      "9VzTq6j1u/oxtj6sE2v9WvWvq3k3vF3k3q11F6u9W8t1b3h6sDbf8A"
      "WtfW1eW9u+be8vVjqL1u+jeTe8Xq2m4vVvq3lvq3vN2uN18jNlaaaN"
      "l+Y0cW93ZJ4W5J4NtwW8TebN2W3wTeZt5W3wTcbeNt28m4bfGZt5W2"
      "wTeZtsSbfBMbZvJvN28m83jbcTZt5N5u3k3G2bfCNtm8m83b4Ntu8"
      "m22bfCNt22bfCJtzNtw3k2bfEbdvJtg2ybfD/9k="
  )
  image = Image.open(BytesIO(image_data))
except Exception as e:
  image = None

# --- GAME LOOP SETUP ---
# 1. Import asyncio
# 2. Add 'async' before your main function definition
async def main():
  running = True
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

    # --- Your Game Logic & Drawing Code Here ---
    screen.fill((0, 0, 0))

    if image:
      # Convert PIL image to Pygame surface to draw it
      mode = image.mode
      size = image.size
      data = image.tobytes()
      py_image = pygame.image.fromstring(data, size, mode)

      # Center the image on the screen
      img_x = (SCREEN_WIDTH - size[0]) // 2
      img_y = (SCREEN_HEIGHT - size[1]) // 2
      screen.blit(py_image, (img_x, img_y))

    pygame.display.flip()
    clock.tick(60)

    await asyncio.sleep(0)  # 3. CRITICAL: Add this at the VERY END of your while loop


# Run the game using asyncio
asyncio.run(main())  # 4. Initialize the loop