# Wealth-seeking: stated vs revealed preferences

This project will contrast what LLM chatbots say they will do in hypothetical QA scenarios versus what the corresponding LM agents (based on the same models) actually do when put in more realistic versions of those scenarios.


Here's the project description/instructions for this idea (based on the 'Predictability between stated and revealed preferences' project from the [concrete problems in evals](https://docs.google.com/document/d/1gi32-HZozxVimNg5Mhvk4CvW4zq8J12rGmK_j2zxNEg/edit?tab=t.0) doc produced by Apollo research):

- We can test how well models transfer from QA settings to minimally agentic settings that are designed to be semantically very close. Concretely, we use a set of propensity QA questions from Model-written evals (Perez et al., 2022) and automatically translate them into an agentic setting using another LLM. Concretely,
    - Take a big dataset of QA-style evals (I'm going to take the wealth-seeking one from Dev et al., 2024's [github](https://github.com/Sunishchal/model-written-evals/blob/main/improved_datasets/wealth-seeking-inclination.jsonl) -- note this is an improved version of [the original Anthropic model-written evals paper](https://arxiv.org/pdf/2212.09251) from 2022. For more info see [this LW post](https://www.lesswrong.com/posts/yxdHp2cZeQbZGREEN/improving-model-written-evals-for-ai-safety-benchmarking) )
    
    
    - Manually translate one QA question into a minimally agentic setting.
        - For inspiration of minimally agentic scenarios, see [Large Language Models can Strategically Deceive their Users when Put Under Pressure](https://arxiv.org/abs/2311.07590) (Scheurer et al., 2023). -- **Note this is the famous "insider trading" paper**
            - I found a python notebook ([LINK](https://schmatz.github.io/deception-eval-with-inspect/)) on github where someone was porting it over to Inspect. I've cloned this into a separate project and gotten it up and running.
            - _I think I might try to reverse-engineer this because I really like this eval - I'll invent a fake "original" QA version of the eval, then instruct my LM to map other questions from QA to minimally-agentic versions based on that example._
        - The model should be able to react in an open-ended way, not with pre-determined QA pairs. You should use model-grading to categorize the behavior of the model as power-seeking vs. not power-seeking (or whatever tendency you chose).
        - You can use LLM assistance for the translation.
    - Translate a few more scenarios. You can use LLM assistance again. Double-check that you agree with all of these scenarios.
    - Use these scenarios as few-shot prompts and translate the full dataset.
    - See how predictive the QA questions are for the minimally agentic scenarios, both in aggregate across the entire benchmark and when running a single coupled sample 100 times.
    - _I think I might also try a couple of simple jailbreaks for the QA and agent versions and see if the agent version's protections are less robust_


_Talk about BrowserART and the LW post about [safety techniques not transferring to the agent setting](https://www.lesswrong.com/posts/ZoFxTqWRBkyanonyb/current-safety-training-techniques-do-not-fully-transfer-to)_

