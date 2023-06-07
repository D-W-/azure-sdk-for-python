# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
from pathlib import Path

import pytest

from azure.ai.ml import MLClient
from devtools_testutils import AzureRecordedTestCase

tests_root_dir = Path(__file__).parent.parent.parent


@pytest.mark.e2etest
@pytest.mark.pipeline_test
class TestFlow(AzureRecordedTestCase):
    def test_flow(self, client: MLClient):
        from azure.ai.ml.entities._load_functions import load_flow

        local_file = tests_root_dir / "test_configs/flows/classification_accuracy_evaluation/flow.meta.yaml"
        flow = load_flow(source=local_file)

        # TODO: local data support
        flow = client.flows.run_bulk(flow=flow, test_data="azureml:test_data:1")

        flow = client.flows.run_bulk(
            flow=flow,
            test_data="azureml:test_data:1",
            evaluation="azureml:classification_accuracy_evaluation:1",
            ground_truth_column="test_data.answer",
            prediction_column="bulk_test_output.answer",
        )

        client.flows.show_metrics(name=flow.name)
