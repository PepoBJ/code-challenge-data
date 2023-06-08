class ResponseUtil:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def build_results_dict(cursorSQLAlchemyResult):
        data = cursorSQLAlchemyResult.fetchall()

        columns = list(cursorSQLAlchemyResult.keys())

        results_dict = []
        for row in data:
            row_dict = {}
            for i in range(len(columns)):
                row_dict[columns[i]] = row[i]
            results_dict.append(row_dict)

        return results_dict
