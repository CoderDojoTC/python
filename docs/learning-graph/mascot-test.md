---
title: Monty the Python - Mascot Test
description: Test page showing all mascot images and admonition styles for Monty the Python, our pedagogical agent.
---
# Monty the Python — Mascot Test

This page shows all mascot images and admonition styles for reference.
Check that all images have a transparent background and no excessive padding.
The dashed blue border around each image makes the padding visible.

<style>
img { border: 1px dashed blue; }
</style>

## Admonition Tests

!!! mascot-neutral "A Note from Monty"
    ![Monty neutral pose](../../img/mascot/neutral.png){ class="mascot-admonition-img" }
    Here is a friendly note from Monty. This is the **neutral** style, used for general sidebars or introductions.

!!! mascot-welcome "Monty Welcomes You!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Welcome, coder! I'm Monty the Python, and I'm here to help you learn to program. This is the **welcome** style, used at the start of each lesson.

!!! mascot-thinking "Monty's Key Insight"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Let's think this through together! This is the **thinking** style, used to highlight key concepts and important ideas.

!!! mascot-tip "Monty's Tip"
    ![Monty sharing a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    Here is a helpful suggestion from Monty. This is the **tip** style, used for hints and shortcuts.

!!! mascot-warning "Watch Out!"
    ![Monty warning you](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    Watch out for this one — it's a common mistake! This is the **warning** style, used to flag pitfalls.

!!! mascot-encourage "You've Got This!"
    ![Monty encouraging you](../../img/mascot/encouraging.png){ class="mascot-admonition-img" }
    You can do it! I believe in you! This is the **encouraging** style, used when the content gets challenging.

!!! mascot-celebration "Excellent Work!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Congratulations — you made it! This is the **celebration** style, used at the end of lessons.

## Image Padding Tests

Verify there is no excessive padding around the images.
If there is, run `scripts/trim-padding-from-image.py docs/img/mascot/FILENAME.png`.

<div class="grid cards" markdown>

- **Welcome**

    ![](../../img/mascot/welcome.png){ width="150px" }

- **Thinking**

    ![](../../img/mascot/thinking.png){ width="150px" }

- **Tip**

    ![](../../img/mascot/tip.png){ width="150px" }

- **Warning**

    ![](../../img/mascot/warning.png){ width="150px" }

- **Encouraging**

    ![](../../img/mascot/encouraging.png){ width="150px" }

- **Celebration**

    ![](../../img/mascot/celebration.png){ width="150px" }

- **Neutral**

    ![](../../img/mascot/neutral.png){ width="150px" }

</div>
