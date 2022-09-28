from pyabsa.functional import ATEPCModelList
from pyabsa.functional import Trainer, ATEPCTrainer
from pyabsa.functional import ABSADatasetList
from pyabsa.functional import ATEPCConfigManager

atepc_config = ATEPCConfigManager.get_atepc_config_english()

atepc_config.pretrained_bert = 'microsoft/deberta-v3-base'
atepc_config.model = ATEPCModelList.FAST_LCF_ATEPC
dataset_path = ABSADatasetList.Restaurant14
# or your local dataset: dataset_path = 'your local dataset path'

aspect_extractor = ATEPCTrainer(config=atepc_config,
                                dataset=dataset_path,
                                from_checkpoint='',  # set checkpoint to train on the checkpoint.
                                checkpoint_save_mode=1,
                                auto_device=True
                                ).load_trained_model()



from pyabsa.functional import ABSADatasetList
from pyabsa.functional import ATEPCCheckpointManager

examples = ['But the staff was so nice to us .',
            'But the staff was so horrible to us .',
            r'Not only was the food outstanding , but the little ` perks \' were great .',
            'It took half an hour to get our check , which was perfect since we could sit , have drinks and talk !',
            'It was pleasantly uncrowded , the service was delightful , the garden adorable , '
            'the food -LRB- from appetizers to entrees -RRB- was delectable .',
            'How pretentious and inappropriate for MJ Grill to claim that it provides power lunch and dinners !'
            ]

inference_source = ABSADatasetList.Restaurant14
aspect_extractor = ATEPCCheckpointManager.get_aspect_extractor(checkpoint='multilingual2')
atepc_result = aspect_extractor.extract_aspect(inference_source=inference_source,
                                               save_result=True,
                                               print_result=True,  # print the result
                                               pred_sentiment=True,  # Predict the sentiment of extracted aspect terms
                                               )