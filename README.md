# Notion Crypto Price Updater

## Setup Guides

- [Written Guide](https://heygarethevans.notion.site/Setup-Instructions-e907297617104d5d850ca403922413cd)
- [Video Guide](https://www.youtube.com/watch?v=7Yc06t7oY7s)

### Step 1: Copy the Example Variables File

1. Copy the `my_variables.example.yml` file to `my_variables.yml`.
2. Open `my_variables.yml` and configure it as follows:

    ```yaml
    MY_NOTION_SECRET_TOKEN: <insert-your-notion-integration-secret-token>
    ```

### Step 2: Obtain Your Notion Secret Token

To obtain your Notion Secret Token for integration, follow these steps:

1. Go to your [Notion integration page](https://www.notion.so/my-integrations) to create or access your integration.
2. Copy the secret token provided for the integration.

Once you have your token, paste it into the `MY_NOTION_SECRET_TOKEN` field in your `my_variables.yml`.

---

## Notion Table Configuration

### Required Fields

When filling in the Notion table, make sure the following fields are **required**:

- **Name**: The ticker symbol of the cryptocurrency (e.g., "BTC" for Bitcoin).
- **Amount Invested**: The amount you have invested in the cryptocurrency.
- **Number of Coins in Wallet**: The number of coins you hold in your wallet.
- **Price/Coin**: This field should **not** be empty. You can either:

  - Manually input a value (e.g., "0").
  - Or, set a filter rule: `price/coin NOT EMPTY`. This will automatically fill in "0" for any new rows.

---

By following these steps, you'll have your Notion Crypto Price Updater set up and configured correctly. Make sure that your Notion table is well-structured with the required fields, and you'll be ready to go.
