#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function

import humps

__author__ = "bibow"

import logging
import traceback
from typing import Any, Dict, List

from openai_funct_base import OpenAIFunctBase


class AIKnowledgeFunct(OpenAIFunctBase):

    def __init__(self, logger: logging.Logger, **setting: Dict[str, Any]):
        try:
            self.logger = logger
            OpenAIFunctBase.__init__(self, logger, **setting)
        except Exception as e:
            log = traceback.format_exc()
            self.logger.error(log)
            raise e

    def get_results_from_knowledge_rag(
        self, **arguments: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        try:
            self.logger.info(f"Arguments: {arguments}")

            variables = {
                "userQuery": arguments["user_query"],
                "documentSource": self.setting["document_source"],
            }
            results = self.execute_graphql_query(
                "ai_knowledge_graphql", "knowledgeRag", "Query", variables
            )["knowledgeRag"]["results"]

            return humps.decamelize(results)
        except Exception as e:
            log = traceback.format_exc()
            self.logger.error(log)
            return {"error": e.args}
