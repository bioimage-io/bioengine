from hypha_rpc.sync import connect_to_server
import numpy as np


def test_get_service(
        server_url: str="https://hypha.aicell.io",
        workspace_name: str="bioengine-apps",
        service_id: str="micro_sam",
    ):
    client = connect_to_server({"server_url": server_url, "method_timeout": 5})
    assert client

    sid = f"{workspace_name}/{service_id}"
    segment_svc = client.get_service(sid)
    assert segment_svc.config.workspace == workspace_name
    assert segment_svc.get("compute_embedding")
    assert segment_svc.get("segment")
    assert segment_svc.get("reset_embedding")

    assert segment_svc.compute_embedding("vit_b", np.random.rand(256, 256))
    features = segment_svc.segment([[128, 128]], [1])
    assert features
    assert segment_svc.reset_embedding()

if __name__ == "__main__":
    test_get_service()