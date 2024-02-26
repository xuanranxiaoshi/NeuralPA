# Assign the openai keys here to use ChatGPT and GPT3, fill multiple keys to avoid insufficient balances to run the entire experiments
openai_keys = [
    "key1",
    "key2"
]


# Pre-Assign the paths of different data files to avoid passing them into each command
datafiles = {
    # The following files are initial files which are necessary to run the experiments
    "testset_metadata": "testset.json",
    "trainset_metadata": "trainset.json",
    "fixed_examples": "fixed_examples.json",

    # The 10,000 sampled instances from the whole testset
    "testset_sampled_metadata": "testset_randomsampled.json",
    "transformed_testset_sampled_metadata": "testset_randomsampled_transformed.json",

    # The following files can be generated by TypeGen
    "testset_sourcecode": "testset_source.json",
    "trainset_sourcecode": "trainset_source.json",
    "transformed_trainset_metadata": "trainset_transformed.json",
    "transformed_testset_metadata": "testset_transformed.json",
    "testset_regular_masked_code": "testset_masked_source.json",
    "testset_codet5_masked_code": "testset_masked_source_codet5.json",
    "testset_usertypes": "testset_usertypes.json",
    "trainset_usertypes": "trainset_usertypes.json",
    "testset_sliced_sourcecode": "testset_staticsliced_hopHOP.json",
    "trainset_sliced_sourcecode": "trainset_staticsliced_hopHOP.json",
    "similar_domos": "topk_with_label_full_transformed.json",
    "similar_sliced_domos": "topk_with_label_staticsliced_hopHOP_transformed.json",
    "trainset_cots": "trainset_cots_hopHOP.json"
}

# Assign the model of ChatGPT and GPT3 you want to use
chatgpt = "gpt-3.5-turbo"
gpt3 = "text-davinci-003"

# Maximum retries when communication with OpenAI fails
max_retry = 10

# Sleep time between instances to avoid hitting the rate limits of OpenAI
normal_sleep = 3
error_sleep = 5

# Cache folder for pre-trained models
cache_dir = "./transformers"