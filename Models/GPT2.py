from transformers import GPT2LMHeadModel, GPT2Config, GPT2Tokenizer
from Utils import get_chess_tokens, dataset_tokens


GPT2_TYPE = "gpt2"


class GPT2:
    def __init__(self):
        # tokenizer
        self.tokenizer = GPT2Tokenizer.from_pretrained(GPT2_TYPE)

        # special tokens
        self.tokenizer.add_special_tokens({'pad_token': '[PAD]'})
        self.tokenizer.add_special_tokens({'additional_special_tokens': dataset_tokens})

        # chess tokens
        self.tokenizer.add_tokens(get_chess_tokens())

        # model
        configuration = GPT2Config.from_pretrained(GPT2_TYPE)
        self.model = GPT2LMHeadModel.from_pretrained(GPT2_TYPE, config=configuration).cuda()

        self.model.resize_token_embeddings(len(self.tokenizer))
