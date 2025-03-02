# Easypost
This directory contains the manifest-only connector for [`source-easypost`](https://www.easypost.com/).

## Documentation reference:
- Visit [`https://docs.easypost.com/docs/addresses`](https://docs.easypost.com/docs/addresses) for API documentation

## Authentication setup
`EasyPost` uses api key authentication routed as Basic Http, Visit `https://docs.easypost.com/docs/authentication` for getting your api keys.

## Configuration

| Input | Type | Description | Default Value |
|-------|------|-------------|---------------|
| `username` | `string` | API Key. The API Key from your easypost settings |  |
| `start_date` | `string` | Start date.  |  |

## Streams
| Stream Name | Primary Key | Pagination | Supports Full Sync | Supports Incremental |
|-------------|-------------|------------|---------------------|----------------------|
| batches | id | DefaultPaginator | ✅ |  ✅  |
| addresses | id | DefaultPaginator | ✅ |  ❌  |
| trackers | id | DefaultPaginator | ✅ |  ✅  |
| metadata_carriers | name | No pagination | ✅ |  ❌  |
| end_shippers | id | DefaultPaginator | ✅ |  ❌  |
| webhooks | id | DefaultPaginator | ✅ |  ✅  |
| users_children | id | DefaultPaginator | ✅ |  ✅  |
| carrier_accounts | id | DefaultPaginator | ✅ |  ✅  |
| api_keys | id | DefaultPaginator | ✅ |  ❌  |

## Changelog

<details>
  <summary>Expand to review</summary>

| Version          | Date              | Pull Request | Subject        |
|------------------|-------------------|--------------|----------------|
| 0.0.7 | 2025-01-11 | [51082](https://github.com/airbytehq/airbyte/pull/51082) | Update dependencies |
| 0.0.6 | 2024-12-28 | [50573](https://github.com/airbytehq/airbyte/pull/50573) | Update dependencies |
| 0.0.5 | 2024-12-21 | [50036](https://github.com/airbytehq/airbyte/pull/50036) | Update dependencies |
| 0.0.4 | 2024-12-14 | [49511](https://github.com/airbytehq/airbyte/pull/49511) | Update dependencies |
| 0.0.3 | 2024-12-12 | [49184](https://github.com/airbytehq/airbyte/pull/49184) | Update dependencies |
| 0.0.2 | 2024-11-04 | [47654](https://github.com/airbytehq/airbyte/pull/47654) | Update dependencies |
| 0.0.1 | 2024-10-01 | [46287](https://github.com/airbytehq/airbyte/pull/46287) | Initial release by [@btkcodedev](https://github.com/btkcodedev) via Connector Builder |

</details>
