# bestmodel.py
from typing import cast
import numpy as np
import pandas as pd
import torch
from sentence_transformers import SentenceTransformer
from torch.nn.functional import cosine_similarity
import numpy.typing as npt

device = "cuda:0" if torch.cuda.is_available() else "cpu"


class ObjectsTextSimilarity:
    def __init__(self) -> None:
        self.model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

    def fit(self, data: pd.DataFrame) -> None:
        self.data = data
        self.name_text_features = self.data.columns
        vectors: list[torch.Tensor] = [
            cast(torch.Tensor, self.model.encode(series.values, convert_to_tensor=True))
            for _, series in data.items()
        ]
        self.data_embedding = torch.cat(vectors, dim=1)

    def predict(
        self,
        query_object_lst: list[str],
        top_k: int = 10,
        filtr_ind: npt.NDArray[np.int64] | None = None,
    ) -> npt.NDArray[np.int64]:
        query_vector = cast(
            torch.Tensor, self.model.encode(query_object_lst, convert_to_tensor=True, device=device)
        )
        similarities = cosine_similarity(query_vector.view(-1), self.data_embedding).cpu().numpy()

        if filtr_ind is not None:
            similarities[filtr_ind] = -1.0

        top_k_indices = np.argsort(similarities)[: -top_k - 1 : -1]

        return top_k_indices
