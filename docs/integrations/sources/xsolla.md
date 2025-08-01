# Xsolla
The Xsolla Airbyte Connector enables seamless integration between Xsolla and various data destinations. This connector allows you to extract data from Xsolla’s APIs, such as Game Catalog, Virtual Items, Virtual Currency and more.

## Configuration

| Input | Type | Description | Default Value |
|-------|------|-------------|---------------|
| `api_key` | `string` | API Key. Go to Xsolla Dashboard and from company setting get the api_key |  |
| `project_id` | `number` | Project Id. You can find this parameter in your Publisher Account next to the name of the project . Example: 44056 |  |

## Streams
| Stream Name | Primary Key | Pagination | Supports Full Sync | Supports Incremental |
|-------------|-------------|------------|---------------------|----------------------|
| Games Catalog | item_id | DefaultPaginator | ✅ |  ❌  |
| DRM | drm_id | No pagination | ✅ |  ❌  |
| Virtual Items | item_id | DefaultPaginator | ✅ |  ❌  |
| Virtual Currency | item_id | DefaultPaginator | ✅ |  ❌  |
| Virtual Currency Package | item_id | DefaultPaginator | ✅ |  ❌  |
| Bundles | item_id | DefaultPaginator | ✅ |  ❌  |
| Reward Chains | reward_chain_id | DefaultPaginator | ✅ |  ❌  |

## Changelog

<details>
  <summary>Expand to review</summary>

| Version          | Date              | Pull Request | Subject        |
|------------------|-------------------|--------------|----------------|
| 0.0.31 | 2025-07-20 | [63651](https://github.com/airbytehq/airbyte/pull/63651) | Update dependencies |
| 0.0.30 | 2025-07-12 | [63211](https://github.com/airbytehq/airbyte/pull/63211) | Update dependencies |
| 0.0.29 | 2025-07-05 | [62703](https://github.com/airbytehq/airbyte/pull/62703) | Update dependencies |
| 0.0.28 | 2025-06-28 | [62211](https://github.com/airbytehq/airbyte/pull/62211) | Update dependencies |
| 0.0.27 | 2025-06-21 | [61779](https://github.com/airbytehq/airbyte/pull/61779) | Update dependencies |
| 0.0.26 | 2025-06-15 | [61214](https://github.com/airbytehq/airbyte/pull/61214) | Update dependencies |
| 0.0.25 | 2025-05-24 | [60754](https://github.com/airbytehq/airbyte/pull/60754) | Update dependencies |
| 0.0.24 | 2025-05-10 | [59952](https://github.com/airbytehq/airbyte/pull/59952) | Update dependencies |
| 0.0.23 | 2025-05-04 | [59558](https://github.com/airbytehq/airbyte/pull/59558) | Update dependencies |
| 0.0.22 | 2025-04-26 | [58922](https://github.com/airbytehq/airbyte/pull/58922) | Update dependencies |
| 0.0.21 | 2025-04-19 | [58546](https://github.com/airbytehq/airbyte/pull/58546) | Update dependencies |
| 0.0.20 | 2025-04-12 | [58030](https://github.com/airbytehq/airbyte/pull/58030) | Update dependencies |
| 0.0.19 | 2025-04-05 | [57403](https://github.com/airbytehq/airbyte/pull/57403) | Update dependencies |
| 0.0.18 | 2025-03-29 | [56886](https://github.com/airbytehq/airbyte/pull/56886) | Update dependencies |
| 0.0.17 | 2025-03-22 | [56304](https://github.com/airbytehq/airbyte/pull/56304) | Update dependencies |
| 0.0.16 | 2025-03-08 | [55624](https://github.com/airbytehq/airbyte/pull/55624) | Update dependencies |
| 0.0.15 | 2025-03-01 | [55137](https://github.com/airbytehq/airbyte/pull/55137) | Update dependencies |
| 0.0.14 | 2025-02-22 | [54489](https://github.com/airbytehq/airbyte/pull/54489) | Update dependencies |
| 0.0.13 | 2025-02-15 | [54066](https://github.com/airbytehq/airbyte/pull/54066) | Update dependencies |
| 0.0.12 | 2025-02-08 | [53529](https://github.com/airbytehq/airbyte/pull/53529) | Update dependencies |
| 0.0.11 | 2025-02-01 | [53071](https://github.com/airbytehq/airbyte/pull/53071) | Update dependencies |
| 0.0.10 | 2025-01-25 | [52457](https://github.com/airbytehq/airbyte/pull/52457) | Update dependencies |
| 0.0.9 | 2025-01-18 | [51970](https://github.com/airbytehq/airbyte/pull/51970) | Update dependencies |
| 0.0.8 | 2025-01-11 | [51392](https://github.com/airbytehq/airbyte/pull/51392) | Update dependencies |
| 0.0.7 | 2024-12-28 | [50813](https://github.com/airbytehq/airbyte/pull/50813) | Update dependencies |
| 0.0.6 | 2024-12-21 | [50350](https://github.com/airbytehq/airbyte/pull/50350) | Update dependencies |
| 0.0.5 | 2024-12-14 | [49762](https://github.com/airbytehq/airbyte/pull/49762) | Update dependencies |
| 0.0.4 | 2024-12-12 | [49392](https://github.com/airbytehq/airbyte/pull/49392) | Update dependencies |
| 0.0.3 | 2024-11-04 | [48219](https://github.com/airbytehq/airbyte/pull/48219) | Update dependencies |
| 0.0.2 | 2024-10-28 | [47595](https://github.com/airbytehq/airbyte/pull/47595) | Update dependencies |
| 0.0.1 | 2024-10-01 | | Initial release by [@avirajsingh7](https://github.com/avirajsingh7) via Connector Builder |

</details>
