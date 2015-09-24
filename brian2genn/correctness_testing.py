'''
Definitions of theconfiguration for correctness testing.
'''
import brian2
import os
import shutil
import sys
import brian2genn
from brian2.tests.features import (Configuration, DefaultConfiguration,
                                   run_feature_tests, run_single_feature_test)

__all__ = ['GeNNConfiguration',
           'GeNNConfigurationOptimized']

class GeNNConfiguration(Configuration):
    name = 'GeNN'
    def before_run(self):
        brian2.prefs.reset_to_defaults()
        brian2.prefs.codegen.loop_invariant_optimisations = False
        brian2.prefs.devices.genn.unix_compiler_flags=''
        windows_compiler_flags=''
        brian2.set_device('genn')
        
    def after_run(self):
        if os.path.exists('GeNNworkspace'):
            shutil.rmtree('GeNNworkspace')
        brian2.device.build(directory='GeNNworkspace', compile=True, run=True,
                            use_GPU=True)

class GeNNConfigurationOptimized(Configuration):
    name = 'GeNN'
    def before_run(self):
        brian2.prefs.reset_to_defaults()
        brian2.prefs.codegen.loop_invariant_optimisations = False
        brian2.set_device('genn')
        
    def after_run(self):
        if os.path.exists('GeNNworkspace'):
            shutil.rmtree('GeNNworkspace')
        brian2.device.build(directory='GeNNworkspace', compile=True, run=True,
                            use_GPU=True)

