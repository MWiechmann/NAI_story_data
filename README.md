# NAI_story_data
Dataset with stories generated by the [Novel AI (NAI)](https://novelai.net/#/) transformer model Euterpe v2 (fine-tuned Fairseq 13b) with a context window of 2048 tokens.

Novel AI is an online service that uses [transformer models](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)) as "interactive AI storytellers".

This dataset contains texts generated with NAI using 4 different starting prompts (representing different "genres") and 8 different generations settings, going through 30 generations by the model. Texts were generated by using the [Novel AI Research Tool (`nrt`)](https://github.com/wbrown/novelai-research-tool).

**Note: Due to the nature of random AI text generation, there is no way reliably control the content of the outputs. Some texts might contain graphic description of violence, sexual acts or other unwanted content.**

You can find the dataset as csv- and excel-file here [here](https://github.com/MWiechmann/NAI_story_data/tree/main/dataset).\
Input files for `nrt` used to generate the texts can be found [here](https://github.com/MWiechmann/NAI_story_data/tree/main/nrt_input_files).

# The prompts
The intitial context (input text) for the generation of texts consisted of 4 different memory + prompt pairs.

## Memory
The "memory" gets inserted at the very top of every context that is being sent to the model. For these generations, memory was simply filled with a specification of the text's genre. Using a [format that imitates the structure of the fine-tune](https://github.com/TravelingRobot/NAI_Community_Research/wiki/Author's-Notes-for-v3), genre was specified like this: `[ Author: ; Tags: ; Genre: High Fantasy ]`

## Prompt
The "prompt" is the starting text given to the model (just after memory), the beginning of the story so to speak. Of course, as the model generates more and more output the prompt is pushed further to the back and is eventually dropped from the context window. I tried to keep the prompts fairly minimal and open for different directions.

## Memory/Prompt Pairs Used to Generate the Data

| Label | Memory | Prompt |
|---|---|---|
| **Hard Sci-Fi** | \[ Author: ; Tags: ; Genre: Hard Sci-fi \] | "I have a message for you from the president,\" said Dr. Sato, handing over an envelope to me. "He's asking that we meet with him at his office this afternoon." I took it and thanked her before walking out of my apartment building into the bright sun. It was already noon on Mars—the longest day in the year here on the planet." |
| **High Fantasy** | \[ Author: ; Tags: ; Genre: High Fantasy \] | "The sun was high in the sky when they arrived at their destination. The valley of the River Tethys flowed into a wide, shallow lake surrounded by mountains on all sides. A small village sat along its shores with two towers standing guard over it from either side like sentinels. It looked to be deserted but for some smoke rising up out of chimneys and the occasional bird flying overhead or flitting through trees." |
| **Historical Romance** | \[ Author: ; Tags: ; Genre: Historical Romance \] | "The first time he saw her, the sight of her was like a slap across his face. She'd come into the tavern where he worked and sat at one of the tables in front of him." |
| **Horror** | \[ Author: ; Tags: ; Genre: Horror \] | "I woke up to hear knocking on glass. At first, I thought it was the window until I heard it come from the mirror again. I got out of bed and walked over to the mirror. When I looked into it, there was a face looking back at me." |

# Generations Settings
Texts were generated by using 8 of the 9 "presets" available at NAI (pre-configured settings). The Moonlit preset was not used to generate the texts, because it employs Top-A Sampling, which is not yet supported by `nrt` (Top-A is a sampling method developed by Novel AI).

## Specifications of the Generation Settings
| label | Temperature | max_length | min_length | top_k | top_p | top_a | tail_free_sampling | repetition_penalty | repetition_penalty_range | repetition_penalty_slope | repetition_penalty_frequency | repetition_penalty_presence | order |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ace of Spade (14/02/2022) | 1.15 | 40 | 1 | 0 | 0.95 | 1 | 0.8 | 2.75 | 2048 | 7.02 | 0 | 0 | TFS, Top-p, Top-k, Temperature |
| All-Nighter (14/02/2022) | 1.33 | 40 | 1 | 13 | 1 | 1 | 0.836 | 2.366 | 400 | 0.33 | 0.01 | 0 | TFS, Top-p, Top-k, Temperature |
| Basic Coherence (14/02/2022) | 0.585 | 40 | 1 | 0 | 1 | 1 | 0.87 | 3.05 | 2048 | 0.33 | 0 | 0 | Temperature, Top-k, Top-p, TFS |
| Fandango (14/02/2022) | 0.86 | 40 | 1 | 20 | 0.95 | 1 | 1 | 2.25 | 2048 | 0.09 | 0 | 0 | Top-p, Top-k, TFS, Temperature |
| Genesis (14/02/2022) |  0.63 | 40 | 1 | 0 | 0.975 | 1 | 0.975 | 2.975 | 2048 | 0.09 | 0 | 0 | Top-p, Top-k, TFS, Temperature |
| Low Rider (14/02/2022) |  0.94 | 40 | 1 | 12 | 1 | 1 | 0.94 | 2.66 | 2048 | 0.18 | 0.013 | 0 | Top-p, Top-k, TFS, Temperature |
| Morpho (14/02/2022) | 0.6889 | 40 | 1 | 0 | 1 | 1 | 1 | 1 | 2048 | 0 | 0.1 | 0 | Temperature, Top-k, Top-p, TFS |
| Ouroboros (14/02/2022) | 1.07 | 40 | 1 | 264 | 1 | 1 | 0.925 | 2.165 | 404 | 0.84 | 0 | 0 | Top-k, Temperature, TFS, Top-p |
