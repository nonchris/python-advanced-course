# Advanced Python Course

A five day lecture I held at the Computer Science department at University Bonn.

The course was a voluntary offering for interested students.
It didn't end with an exam and didn't give any credit points.

The target demographic for this lecture were computer science students with at least two semesters of experience.

The lecture was held in german in 2023 and 2024 and was translated to english in 2025.

Most content was initially created in the Summer of 2023 and then updated and improved for the subsequent years.
No AI was used for content creation.

The main folder you probably wanna look at is `compiled_2525/`.

## Topics
Day 1.: Quick introduction to Python basics and more advanced syntax

Day 2.: FastAPI, Requests, Pydantic, Packaging

Day 3.: Python's Science Stack (numpy, matplotlib, pandas)

Day 4.: Multithreading, Multiprocessing, Iter- and Functools

Day 5.: LLM-Agents using PydanticAI, Rich, AsyncIO

Appendix.: Things that were swapped out to make place for PydanticAI (only german)

## Repo Structure
`vorlesung_XXXX/` are the source files for each lecture for that year.

`uebung_XXXX/` are the source files for each exercise sheet for that year.

`src/` contains all source files for examples I used over the years.

`compiled_2525/` contains the latest versions of all slides and exercise sheets.

## Tasks & Demos
The requirements for 2025 can be found in: `requirements_2025.txt`


## Building the slides & tasks
From `vorlesung_2525`:

`latexmk -lualatex -interaction=nonstopmode "python_vertiefung_XX.tex"`

From `uebung_2525`:
`latexmk -pdf -interaction=nonstopmode "zettel_XX.tex"`

Note.:

The original template was removed due to licensing issues.
The new template was created using AI, to have a drop-in replacement.

I made sure that the 2025 edition is compilable.
The old editions are not migrated to the new template.
So you'd have to migrate them yourself if you need it.

If you want the slides in the original design, please refer to `compiled_2525/`.

# Credits
The course was mainly designed by myself, voluntarily without getting paid for creating it.

We had varying funds over the years, to hire some fellow CS students as tutors, assisting with the exercise sessions.

I'm super greatful for the awesome teams I had over the years.
Everyone was always motivated and ready to assist when we needed someone for proof-reading or similar tasks.


### 2023

Adrian Oeyen helped write the initial slides of day 1 and 4.

Mathilde Schreck & Adrian Oeyen contributed to the creation of the initial exercise sheets.

Both were hired as tutors. I'm very grateful that Adrian did a lot more than he was hired for.

I was also hired as a tutor in that year.

### 2024

Tutors:
- Konstantin Hirschfeld
- Miguel Cortina Zapp
- Linus Rodríguez Gómez

I was hired as lecturer and tutor.

### 2025
- Sophia Sirtl (co-lecturer & tutor)
- Miguel Cortina Zapp
- Jonas Reif

I was hired as lecturer and tutor.

# AI disclosure
- The template to make the slides of 2025 render without the original template was created by AI.
- The translation from german to english was AI assisted.

All other aspects of this lecture are 'handmade'.
