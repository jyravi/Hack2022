from azureml.automl.dnn.nlp.classification.multiclass import runner

automl_settings = {'enable_early_stopping':True,'enable_ensembling':True,'enable_stack_ensembling':True,'ensemble_iterations':15,'enable_onnx_compatible_models':False,'max_cores_per_iteration':-1,'send_telemetry':True,'blacklist_algos':['TensorFlowDNN','TensorFlowLinearRegressor'],'whitelist_models':None,'compute_target':'gpu-cluster-V100','enable_dnn':True,'enable_code_generation':False,'experiment_exit_score':None,'experiment_timeout_minutes':1440,'featurization':{'_blocked_transformers':[],'_column_purposes':{},'_transformer_params':{'Imputer':[]},'_drop_columns':None,'_dataset_language':'eng'},'hyperdrive_config':None,'grain_column_names':None,'is_timeseries':False,'iteration_timeout_minutes':1440,'max_concurrent_iterations':1,'metric_operation':'maximize','model_explainability':True,'n_cross_validations':None,'name':'emailcategory','path':'./sample_projects/emailcategory','primary_metric':'accuracy','region':'eastus2','resource_group':'testFeast','subscription_id':'225d6361-069a-4dfb-9bbb-3ebb42663de0','task_type':'text-classification','validation_size':None,'test_size':None,'vm_type':'STANDARD_NC6S_V3','workspace_name':'mlqsrwdadqzph7i','label_column_name':'label','save_mlflow':True,'enable_batch_run':True,'dataset_id':'c1ecb904-f222-4413-8dbb-e53a09bd66af','validation_dataset_id':'042a3d2d-c272-4d2c-b091-11c3f81dccba', 'is_gpu': True} # PLACEHOLDER
mltable_data_json = None # PLACEHOLDER

if __name__ == '__main__':
    if mltable_data_json:
        runner.run(automl_settings=automl_settings,
                   mltable_data_json=mltable_data_json)
    else:
        runner.run(automl_settings=automl_settings)
