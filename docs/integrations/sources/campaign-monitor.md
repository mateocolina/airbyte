# Campaign Monitor

This is the setup for the Campaign Monitor source which ingests data from the campaign monitor api.
The different types of `campaign` endpoints are available in this source.

## Prerequisites

A username and password associated with your Campaign Monitor account is required for authentication.
You can get your API key from the Account Settings page when logged into your Campaign Monitor account. 
Enter the API key in the username field and enter any value in the password field https://www.campaignmonitor.com/api/v3-3/getting-started/ 

You can specify a `start_date` for replicating data from the beginning of that date.

## Set up the Adjust source connector

1. Click **Sources** and then click **+ New source**.
2. On the Set up the source page, select **Campaign Monitor** from the Source type dropdown.
3. Enter a name for your new source.
4. For **username**, enter your API key obtained in the previous step.
5. For **password**, enter your any dummy value.
6. For **start_date**, enter a date in YYYY-MM-DD format (UTC timezone is assumed). Data starting from this date will be replicated.
8. Click **Set up source**.

## Supported sync modes

The source connector supports the following [sync modes](https://docs.airbyte.com/cloud/core-concepts#connection-sync-modes):

- Full Refresh
- Incremental

## Configuration

| Input | Type | Description | Default Value |
|-------|------|-------------|---------------|
| `username` | `string` | Username.  |  |
| `password` | `string` | Password.  |  |
| `start_date` | `string` | start_date. Date from when the sync should start |  |

## Streams
| Stream Name | Primary Key | Pagination | Supports Full Sync | Supports Incremental |
|-------------|-------------|------------|---------------------|----------------------|
| clients | ClientID | No pagination | ✅ |  ❌  |
| admins | EmailAddress | No pagination | ✅ |  ❌  |
| client_details | ClientID | No pagination | ✅ |  ❌  |
| segments | SegmentID | No pagination | ✅ |  ❌  |
| templates | TemplateID | No pagination | ✅ |  ❌  |
| people | EmailAddress | No pagination | ✅ |  ❌  |
| tags | Name | No pagination | ✅ |  ❌  |
| subscriber_lists | ListID | No pagination | ✅ |  ❌  |
| suppression_lists | EmailAddress | DefaultPaginator | ✅ |  ❌  |
| sent_campaigns | CampaignID | DefaultPaginator | ✅ |  ✅  |
| draft_campaigns | CampaignID | No pagination | ✅ |  ❌  |
| scheduled_campaigns | CampaignID  | No pagination | ✅ |  ❌  |

## Changelog

<details>
  <summary>Expand to review</summary>

| Version          | Date              | Pull Request | Subject        |
|------------------|-------------------|--------------|----------------|
| 0.0.26 | 2025-07-12 | [63074](https://github.com/airbytehq/airbyte/pull/63074) | Update dependencies |
| 0.0.25 | 2025-07-05 | [62536](https://github.com/airbytehq/airbyte/pull/62536) | Update dependencies |
| 0.0.24 | 2025-06-28 | [60603](https://github.com/airbytehq/airbyte/pull/60603) | Update dependencies |
| 0.0.23 | 2025-05-10 | [59354](https://github.com/airbytehq/airbyte/pull/59354) | Update dependencies |
| 0.0.22 | 2025-04-26 | [58698](https://github.com/airbytehq/airbyte/pull/58698) | Update dependencies |
| 0.0.21 | 2025-04-19 | [58291](https://github.com/airbytehq/airbyte/pull/58291) | Update dependencies |
| 0.0.20 | 2025-04-12 | [57635](https://github.com/airbytehq/airbyte/pull/57635) | Update dependencies |
| 0.0.19 | 2025-04-05 | [57152](https://github.com/airbytehq/airbyte/pull/57152) | Update dependencies |
| 0.0.18 | 2025-03-29 | [56625](https://github.com/airbytehq/airbyte/pull/56625) | Update dependencies |
| 0.0.17 | 2025-03-22 | [56108](https://github.com/airbytehq/airbyte/pull/56108) | Update dependencies |
| 0.0.16 | 2025-03-08 | [55355](https://github.com/airbytehq/airbyte/pull/55355) | Update dependencies |
| 0.0.15 | 2025-03-01 | [54882](https://github.com/airbytehq/airbyte/pull/54882) | Update dependencies |
| 0.0.14 | 2025-02-22 | [54259](https://github.com/airbytehq/airbyte/pull/54259) | Update dependencies |
| 0.0.13 | 2025-02-15 | [53878](https://github.com/airbytehq/airbyte/pull/53878) | Update dependencies |
| 0.0.12 | 2025-02-08 | [53414](https://github.com/airbytehq/airbyte/pull/53414) | Update dependencies |
| 0.0.11 | 2025-02-01 | [52948](https://github.com/airbytehq/airbyte/pull/52948) | Update dependencies |
| 0.0.10 | 2025-01-25 | [52164](https://github.com/airbytehq/airbyte/pull/52164) | Update dependencies |
| 0.0.9 | 2025-01-18 | [51737](https://github.com/airbytehq/airbyte/pull/51737) | Update dependencies |
| 0.0.8 | 2025-01-11 | [51264](https://github.com/airbytehq/airbyte/pull/51264) | Update dependencies |
| 0.0.7 | 2024-12-28 | [50476](https://github.com/airbytehq/airbyte/pull/50476) | Update dependencies |
| 0.0.6 | 2024-12-21 | [50185](https://github.com/airbytehq/airbyte/pull/50185) | Update dependencies |
| 0.0.5 | 2024-12-14 | [49581](https://github.com/airbytehq/airbyte/pull/49581) | Update dependencies |
| 0.0.4 | 2024-12-12 | [49002](https://github.com/airbytehq/airbyte/pull/49002) | Update dependencies |
| 0.0.3 | 2024-11-04 | [48232](https://github.com/airbytehq/airbyte/pull/48232) | Update dependencies |
| 0.0.2 | 2024-10-28 | [47643](https://github.com/airbytehq/airbyte/pull/47643) | Update dependencies |
| 0.0.1 | 2024-10-05 | | Initial release by [@aazam-gh](https://github.com/aazam-gh) via Connector Builder |

</details>
