# ClickUp API

## Sync overview

This source can sync data from [ClickUp API](https://clickup.com/api/). Currently, this connector only supports full refresh syncs. That is, every time a sync is run, all the records are fetched from the source.

### Output schema

This source is capable of syncing the following streams:

- [`user`](https://clickup.com/api/clickupreference/operation/GetAuthorizedUser/)
- [`teams`](https://clickup.com/api/clickupreference/operation/GetAuthorizedTeams/)
- [`spaces`](https://clickup.com/api/clickupreference/operation/GetSpaces/)
- [`space_tags`](https://clickup.com/api/clickupreference/operation/GetSpaceTags/)
- [`folders`](https://clickup.com/api/clickupreference/operation/GetFolders/)
- [`lists`](https://clickup.com/api/clickupreference/operation/GetLists/)
- [`list_custom_fields`](https://clickup.com/api/clickupreference/operation/GetAccessibleCustomFields/)
- [`list_comments`](https://clickup.com/api/clickupreference/operation/GetAccessibleCustomFields/)
- [`tasks`](https://clickup.com/api/clickupreference/operation/GetTasks)
- [`time_tracking`](https://clickup.com/api/clickupreference/operation/Gettrackedtime/)
- [`time_tracking_tags`](https://clickup.com/api/clickupreference/operation/Getalltagsfromtimeentries/)
- [`team_goals`](https://clickup.com/api/clickupreference/operation/GetGoals/)
- [`team_custom_fields`](https://clickup.com/api/clickupreference/operation/getTeamAvailableFields/)


### Features

| Feature           | Supported? \(Yes/No\) | Notes |
| :---------------- | :-------------------- | :---- |
| Full Refresh Sync | Yes                   |       |
| Incremental Sync  | No                    |       |

### Performance considerations

The ClickUp API enforces request rate limits per token. The rate limits are depending on your workplace plan. See [here](https://clickup.com/api/developer-portal/rate-limits/).

## Getting started

### Requirements

1. Generate an API key from [ClickUp](https://clickup.com/). See [here](https://clickup.com/api/developer-portal/authentication/#generate-your-personal-api-token).

### Setup guide

The following fields are required fields for the connector to work:

- `api_token`: Your ClickUp API Token.

Here are some optional fields:

- `Include Closed Tasks`: Toggle to include or exclude closed tasks. By default, they are excluded.

## Changelog

<details>
  <summary>Expand to review</summary>

| Version | Date       | Pull Request                                             | Subject                           |
| :------ | :--------- | :------------------------------------------------------- | :-------------------------------- |
| 0.3.27 | 2025-07-19 | [63540](https://github.com/airbytehq/airbyte/pull/63540) | Update dependencies |
| 0.3.26 | 2025-07-12 | [62971](https://github.com/airbytehq/airbyte/pull/62971) | Update dependencies |
| 0.3.25 | 2025-07-05 | [62769](https://github.com/airbytehq/airbyte/pull/62769) | Update dependencies |
| 0.3.24 | 2025-06-28 | [62420](https://github.com/airbytehq/airbyte/pull/62420) | Update dependencies |
| 0.3.23 | 2025-06-21 | [61938](https://github.com/airbytehq/airbyte/pull/61938) | Update dependencies |
| 0.3.22 | 2025-06-14 | [60023](https://github.com/airbytehq/airbyte/pull/60023) | Update dependencies |
| 0.3.21 | 2025-05-03 | [59401](https://github.com/airbytehq/airbyte/pull/59401) | Update dependencies |
| 0.3.20 | 2025-04-26 | [58836](https://github.com/airbytehq/airbyte/pull/58836) | Update dependencies |
| 0.3.19 | 2025-04-19 | [58352](https://github.com/airbytehq/airbyte/pull/58352) | Update dependencies |
| 0.3.18 | 2025-04-12 | [57806](https://github.com/airbytehq/airbyte/pull/57806) | Update dependencies |
| 0.3.17 | 2025-04-05 | [57202](https://github.com/airbytehq/airbyte/pull/57202) | Update dependencies |
| 0.3.16 | 2025-03-29 | [56486](https://github.com/airbytehq/airbyte/pull/56486) | Update dependencies |
| 0.3.15 | 2025-03-22 | [55972](https://github.com/airbytehq/airbyte/pull/55972) | Update dependencies |
| 0.3.14 | 2025-03-08 | [55416](https://github.com/airbytehq/airbyte/pull/55416) | Update dependencies |
| 0.3.13 | 2025-03-01 | [54905](https://github.com/airbytehq/airbyte/pull/54905) | Update dependencies |
| 0.3.12 | 2025-02-22 | [54266](https://github.com/airbytehq/airbyte/pull/54266) | Update dependencies |
| 0.3.11 | 2025-02-15 | [53901](https://github.com/airbytehq/airbyte/pull/53901) | Update dependencies |
| 0.3.10 | 2025-02-08 | [53413](https://github.com/airbytehq/airbyte/pull/53413) | Update dependencies |
| 0.3.9 | 2025-02-01 | [52928](https://github.com/airbytehq/airbyte/pull/52928) | Update dependencies |
| 0.3.8 | 2025-01-25 | [52209](https://github.com/airbytehq/airbyte/pull/52209) | Update dependencies |
| 0.3.7 | 2025-01-18 | [51739](https://github.com/airbytehq/airbyte/pull/51739) | Update dependencies |
| 0.3.6 | 2025-01-11 | [51243](https://github.com/airbytehq/airbyte/pull/51243) | Update dependencies |
| 0.3.5 | 2024-12-28 | [50474](https://github.com/airbytehq/airbyte/pull/50474) | Update dependencies |
| 0.3.4 | 2024-12-21 | [50199](https://github.com/airbytehq/airbyte/pull/50199) | Update dependencies |
| 0.3.3 | 2024-12-14 | [49579](https://github.com/airbytehq/airbyte/pull/49579) | Update dependencies |
| 0.3.2 | 2024-12-12 | [47873](https://github.com/airbytehq/airbyte/pull/47873) | Update dependencies |
| 0.3.1 | 2024-10-28 | [47636](https://github.com/airbytehq/airbyte/pull/47636) | Update dependencies |
| 0.3.0 | 2024-08-19 | [44430](https://github.com/airbytehq/airbyte/pull/44430) | Refactor connector to manifest-only format |
| 0.2.0 | 2024-08-19 | [44180](https://github.com/airbytehq/airbyte/pull/44180) | Add `time_tracking`, `time_tracking_tags`, `team_goals`, `space_tags`, `team_custom_fields`, `list_custom_fields`, `list_comments`, Parent ids passed from responses, Add error handlers |
| 0.1.13 | 2024-08-17 | [44237](https://github.com/airbytehq/airbyte/pull/44237) | Update dependencies |
| 0.1.12 | 2024-08-12 | [43844](https://github.com/airbytehq/airbyte/pull/43844) | Update dependencies |
| 0.1.11 | 2024-08-10 | [43065](https://github.com/airbytehq/airbyte/pull/43065) | Update dependencies |
| 0.1.10 | 2024-07-27 | [42647](https://github.com/airbytehq/airbyte/pull/42647) | Update dependencies |
| 0.1.9 | 2024-07-20 | [41927](https://github.com/airbytehq/airbyte/pull/41927) | Update dependencies |
| 0.1.8 | 2024-07-15 | [38344](https://github.com/airbytehq/airbyte/pull/38344) | Make connector compatible with builder |
| 0.1.7 | 2024-07-10 | [41397](https://github.com/airbytehq/airbyte/pull/41397) | Update dependencies |
| 0.1.6 | 2024-07-09 | [41301](https://github.com/airbytehq/airbyte/pull/41301) | Update dependencies |
| 0.1.5 | 2024-07-06 | [40936](https://github.com/airbytehq/airbyte/pull/40936) | Update dependencies |
| 0.1.4 | 2024-06-25 | [40478](https://github.com/airbytehq/airbyte/pull/40478) | Update dependencies |
| 0.1.3 | 2024-06-22 | [40061](https://github.com/airbytehq/airbyte/pull/40061) | Update dependencies |
| 0.1.2 | 2024-05-21 | [38501](https://github.com/airbytehq/airbyte/pull/38501) | [autopull] base image + poetry + up_to_date |
| 0.1.1 | 2023-02-10 | [23951](https://github.com/airbytehq/airbyte/pull/23951) | Add optional include Closed Tasks |
| 0.1.0 | 2022-11-07 | [17770](https://github.com/airbytehq/airbyte/pull/17770) | New source |

</details>
