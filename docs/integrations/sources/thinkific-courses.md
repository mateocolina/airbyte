# Thinkific Courses

Thinkific is a leading platform for creating, marketing, and selling courses, digital products, communities and learning experiences.
This connector retrives basic data information from courses.

## Configuration

| Input | Type | Description | Default Value |
|-------|------|-------------|---------------|
| `api_key` | `string` | API Key.  |  |
| `X-Auth-Subdomain` | `string` | subdomain.  |  |

## Streams
| Stream Name | Primary Key | Pagination | Supports Full Sync | Supports Incremental |
|-------------|-------------|------------|---------------------|----------------------|
| Courses |  | DefaultPaginator | ✅ |  ❌  |
| Courses Chapters |  | DefaultPaginator | ✅ |  ❌  |
| Contents |  | DefaultPaginator | ✅ |  ❌  |

## Changelog

<details>
  <summary>Expand to review</summary>

| Version          | Date              | Pull Request | Subject        |
|------------------|-------------------|--------------|----------------|
| 0.0.15 | 2025-07-19 | [63612](https://github.com/airbytehq/airbyte/pull/63612) | Update dependencies |
| 0.0.14 | 2025-07-12 | [63061](https://github.com/airbytehq/airbyte/pull/63061) | Update dependencies |
| 0.0.13 | 2025-06-28 | [62271](https://github.com/airbytehq/airbyte/pull/62271) | Update dependencies |
| 0.0.12 | 2025-06-21 | [61804](https://github.com/airbytehq/airbyte/pull/61804) | Update dependencies |
| 0.0.11 | 2025-06-14 | [61470](https://github.com/airbytehq/airbyte/pull/61470) | Update dependencies |
| 0.0.10 | 2025-05-24 | [60490](https://github.com/airbytehq/airbyte/pull/60490) | Update dependencies |
| 0.0.9 | 2025-05-10 | [60163](https://github.com/airbytehq/airbyte/pull/60163) | Update dependencies |
| 0.0.8 | 2025-05-04 | [59605](https://github.com/airbytehq/airbyte/pull/59605) | Update dependencies |
| 0.0.7 | 2025-04-27 | [58384](https://github.com/airbytehq/airbyte/pull/58384) | Update dependencies |
| 0.0.6 | 2025-04-12 | [57990](https://github.com/airbytehq/airbyte/pull/57990) | Update dependencies |
| 0.0.5 | 2025-04-05 | [57419](https://github.com/airbytehq/airbyte/pull/57419) | Update dependencies |
| 0.0.4 | 2025-03-29 | [56325](https://github.com/airbytehq/airbyte/pull/56325) | Update dependencies |
| 0.0.3 | 2025-03-08 | [55630](https://github.com/airbytehq/airbyte/pull/55630) | Update dependencies |
| 0.0.2 | 2025-03-01 | [55089](https://github.com/airbytehq/airbyte/pull/55089) | Update dependencies |
| 0.0.1 | 2025-02-20 | | Initial release by [@gueroverde](https://github.com/gueroverde) via Connector Builder |

</details>
