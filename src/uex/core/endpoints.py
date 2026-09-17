"""Every GET endpoint the API exposes, with its auth, caching, and parameter rules."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import timedelta

MINUTE = timedelta(minutes=1)
HALF_HOUR = timedelta(minutes=30)
HOUR = timedelta(hours=1)
TWELVE_HOURS = timedelta(hours=12)
DAY = timedelta(days=1)

# auth levels
PUBLIC = "public"
TOKEN = "token"
SECRET = "secret"  # implies TOKEN


@dataclass(frozen=True)
class Endpoint:
    name: str
    path: str
    auth: str = PUBLIC
    ttl: timedelta | None = None
    params: tuple[str, ...] = ()
    requires: tuple[str, ...] = ()
    """("any"|"all", *param_names), or () for no requirement."""
    multi: tuple[str, ...] = ()
    """Params that accept up to 10 comma-separated ids."""
    single: bool = False
    """True when ``data`` is one object rather than a list."""
    model: str = ""


def _e(
    name: str,
    path: str,
    model: str,
    *,
    auth: str = PUBLIC,
    ttl: timedelta | None = None,
    params: tuple[str, ...] = (),
    requires: tuple[str, ...] = (),
    multi: tuple[str, ...] = (),
    single: bool = False,
) -> Endpoint:
    return Endpoint(
        name=name,
        path=path,
        auth=auth,
        ttl=ttl,
        params=params,
        requires=requires,
        multi=multi,
        single=single,
        model=model,
    )


_ALL: tuple[Endpoint, ...] = (
    # -- categories / items -------------------------------------------------
    _e("categories", "categories", "Category", ttl=DAY, params=("type", "section")),
    _e(
        "categories_attributes",
        "categories_attributes",
        "CategoryAttribute",
        ttl=DAY,
        params=("id_category",),
    ),
    _e(
        "items",
        "items",
        "Item",
        ttl=DAY,
        params=("id_category", "id_company", "uuid", "size"),
        requires=("any", "id_category", "id_company", "uuid", "size"),
    ),
    _e(
        "items_attributes",
        "items_attributes",
        "ItemAttribute",
        ttl=DAY,
        params=("id_item", "id_category", "uuid"),
        requires=("any", "id_item", "id_category", "uuid"),
    ),
    _e(
        "items_prices",
        "items_prices",
        "ItemPrice",
        ttl=DAY,
        params=("id_terminal", "id_item", "id_category", "uuid"),
        requires=("any", "id_terminal", "id_item", "id_category", "uuid"),
        multi=("id_terminal",),
    ),
    _e("items_prices_all", "items_prices_all", "ItemPriceSummary", ttl=TWELVE_HOURS),
    # -- commodities ----------------------------------------------------------
    _e("commodities", "commodities", "Commodity", ttl=HOUR),
    _e(
        "commodities_alerts",
        "commodities_alerts",
        "CommodityAlert",
        ttl=HALF_HOUR,
        params=("id_commodity",),
    ),
    _e(
        "commodities_averages",
        "commodities_averages",
        "CommodityAverage",
        auth=TOKEN,
        ttl=HALF_HOUR,
        params=("id_commodity",),
        requires=("all", "id_commodity"),
    ),
    _e(
        "commodities_prices",
        "commodities_prices",
        "CommodityPrice",
        ttl=HALF_HOUR,
        params=(
            "id_terminal",
            "id_commodity",
            "terminal_name",
            "terminal_code",
            "terminal_slug",
            "commodity_name",
            "commodity_code",
            "commodity_slug",
        ),
        requires=(
            "any",
            "id_terminal",
            "id_commodity",
            "terminal_name",
            "terminal_code",
            "terminal_slug",
            "commodity_name",
            "commodity_code",
            "commodity_slug",
        ),
        multi=("id_terminal",),
    ),
    _e("commodities_prices_all", "commodities_prices_all", "CommodityPriceSummary", ttl=HALF_HOUR),
    _e(
        "commodities_prices_history",
        "commodities_prices_history",
        "CommodityPriceHistory",
        ttl=TWELVE_HOURS,
        params=("id_terminal", "id_commodity", "game_version"),
    ),
    _e("commodities_ranking", "commodities_ranking", "CommodityRanking", ttl=HALF_HOUR),
    _e(
        "commodities_raw_averages",
        "commodities_raw_averages",
        "CommodityRawAverage",
        ttl=HALF_HOUR,
        params=("id_commodity",),
        requires=("all", "id_commodity"),
    ),
    _e(
        "commodities_raw_prices",
        "commodities_raw_prices",
        "CommodityRawPrice",
        ttl=HALF_HOUR,
        params=("id_terminal", "id_commodity"),
        requires=("any", "id_terminal", "id_commodity"),
        multi=("id_terminal",),
    ),
    _e(
        "commodities_raw_prices_all",
        "commodities_raw_prices_all",
        "CommodityRawPriceSummary",
        ttl=HALF_HOUR,
    ),
    _e(
        "commodities_routes",
        "commodities_routes",
        "CommodityRoute",
        ttl=HALF_HOUR,
        params=(
            "id_terminal_origin",
            "id_planet_origin",
            "id_orbit_origin",
            "id_commodity",
            "id_terminal_destination",
            "id_planet_destination",
            "id_orbit_destination",
            "id_faction_origin",
            "id_faction_destination",
            "investment",
        ),
        requires=(
            "any",
            "id_terminal_origin",
            "id_planet_origin",
            "id_orbit_origin",
            "id_commodity",
        ),
    ),
    _e("commodities_status", "commodities_status", "CommodityStatus", ttl=DAY),
    # -- fuel -------------------------------------------------------------
    _e(
        "fuel_prices",
        "fuel_prices",
        "FuelPrice",
        ttl=HALF_HOUR,
        params=(
            "id_terminal",
            "id_commodity",
            "terminal_name",
            "terminal_code",
            "terminal_slug",
            "commodity_name",
            "commodity_code",
            "commodity_slug",
        ),
        requires=(
            "any",
            "id_terminal",
            "id_commodity",
            "terminal_name",
            "terminal_code",
            "terminal_slug",
            "commodity_name",
            "commodity_code",
            "commodity_slug",
        ),
        multi=("id_terminal",),
    ),
    _e("fuel_prices_all", "fuel_prices_all", "FuelPriceSummary", ttl=HALF_HOUR),
    # -- vehicles -----------------------------------------------------------
    _e("vehicles", "vehicles", "Vehicle", ttl=TWELVE_HOURS, params=("id_company",)),
    _e(
        "vehicles_loaners",
        "vehicles_loaners",
        "VehicleLoaner",
        ttl=TWELVE_HOURS,
        params=("id_vehicle", "uuid", "name"),
    ),
    _e(
        "vehicles_prices",
        "vehicles_prices",
        "VehiclePrice",
        ttl=TWELVE_HOURS,
        params=("id_vehicle", "uuid"),
    ),
    _e(
        "vehicles_purchases_prices",
        "vehicles_purchases_prices",
        "VehiclePurchasePrice",
        ttl=TWELVE_HOURS,
        params=("id_terminal", "uuid", "id_vehicle"),
        requires=("any", "id_terminal", "uuid", "id_vehicle"),
        multi=("id_terminal",),
    ),
    _e(
        "vehicles_purchases_prices_all",
        "vehicles_purchases_prices_all",
        "VehiclePurchasePriceSummary",
        ttl=TWELVE_HOURS,
    ),
    _e(
        "vehicles_rentals_prices",
        "vehicles_rentals_prices",
        "VehicleRentalPrice",
        ttl=TWELVE_HOURS,
        params=("id_terminal", "uuid", "id_vehicle"),
        requires=("any", "id_terminal", "uuid", "id_vehicle"),
        multi=("id_terminal",),
    ),
    _e(
        "vehicles_rentals_prices_all",
        "vehicles_rentals_prices_all",
        "VehicleRentalPriceSummary",
        ttl=TWELVE_HOURS,
    ),
    # -- terminals ------------------------------------------------------------
    _e(
        "terminals",
        "terminals",
        "Terminal",
        ttl=TWELVE_HOURS,
        params=(
            "id_star_system",
            "id_planet",
            "id_orbit",
            "id_moon",
            "id_space_station",
            "id_city",
            "id_outpost",
            "id_poi",
            "id_faction",
            "id_company",
            "type",
            "name",
            "fullname",
            "displayname",
            "code",
        ),
    ),
    _e(
        "terminals_distances",
        "terminals_distances",
        "TerminalDistance",
        ttl=TWELVE_HOURS,
        params=("id_terminal_origin", "id_terminal_destination"),
    ),
    # -- universe -------------------------------------------------------------
    _e("star_systems", "star_systems", "StarSystem", ttl=DAY),
    _e(
        "planets",
        "planets",
        "Planet",
        ttl=DAY,
        params=("id_star_system", "id_faction", "id_jurisdiction", "is_lagrange"),
    ),
    _e(
        "moons",
        "moons",
        "Moon",
        ttl=DAY,
        params=("id_star_system", "id_faction", "id_jurisdiction", "id_planet"),
    ),
    _e(
        "orbits",
        "orbits",
        "Orbit",
        ttl=DAY,
        params=("id_star_system", "id_faction", "id_jurisdiction", "is_lagrange"),
    ),
    _e(
        "orbits_distances",
        "orbits_distances",
        "OrbitDistance",
        ttl=DAY,
        params=(
            "id_star_system",
            "id_star_system_origin",
            "id_star_system_destination",
            "id_orbit_origin",
            "id_orbit_destination",
        ),
    ),
    _e(
        "space_stations",
        "space_stations",
        "SpaceStation",
        ttl=DAY,
        params=(
            "id_star_system",
            "id_faction",
            "id_jurisdiction",
            "id_planet",
            "id_orbit",
            "id_moon",
            "id_city",
        ),
    ),
    _e(
        "cities",
        "cities",
        "City",
        ttl=DAY,
        params=(
            "id_star_system",
            "id_faction",
            "id_jurisdiction",
            "id_planet",
            "id_orbit",
            "id_moon",
        ),
    ),
    _e(
        "outposts",
        "outposts",
        "Outpost",
        ttl=DAY,
        params=(
            "id_star_system",
            "id_faction",
            "id_jurisdiction",
            "id_planet",
            "id_orbit",
            "id_moon",
        ),
    ),
    _e(
        "poi",
        "poi",
        "PointOfInterest",
        ttl=DAY,
        params=(
            "id_star_system",
            "id_faction",
            "id_jurisdiction",
            "id_planet",
            "id_orbit",
            "id_moon",
            "id_space_station",
            "id_city",
            "id_outpost",
        ),
    ),
    _e(
        "jump_points",
        "jump_points",
        "JumpPoint",
        ttl=DAY,
        params=(
            "id_star_system_origin",
            "id_star_system_destination",
            "id_orbit_origin",
            "id_orbit_destination",
        ),
    ),
    _e("jurisdictions", "jurisdictions", "Jurisdiction", ttl=DAY),
    _e("factions", "factions", "Faction", ttl=DAY),
    _e(
        "companies",
        "companies",
        "Company",
        ttl=DAY,
        params=("is_item_manufacturer", "is_vehicle_manufacturer"),
    ),
    _e("contacts", "contacts", "Contact", ttl=DAY),
    _e("contracts", "contracts", "Contract", ttl=DAY),
    # -- marketplace ------------------------------------------------------------
    _e(
        "marketplace_listings",
        "marketplace_listings",
        "MarketplaceListing",
        params=("id", "slug", "username", "id_item", "operation"),
    ),
    _e(
        "marketplace_averages",
        "marketplace_averages",
        "MarketplaceAverage",
        ttl=DAY,
        params=("id_item", "id_category", "uuid"),
        requires=("any", "id_item", "id_category", "uuid"),
    ),
    _e(
        "marketplace_averages_all",
        "marketplace_averages_all",
        "MarketplaceAverageSummary",
        ttl=TWELVE_HOURS,
    ),
    _e(
        "marketplace_favorites",
        "marketplace_favorites",
        "MarketplaceFavorite",
        auth=SECRET,
    ),
    _e(
        "marketplace_negotiations",
        "marketplace_negotiations",
        "MarketplaceNegotiation",
        auth=SECRET,
        params=("id", "id_listing", "hash"),
    ),
    _e(
        "marketplace_negotiations_messages",
        "marketplace_negotiations_messages",
        "MarketplaceNegotiationMessage",
        auth=SECRET,
        params=("id_negotiation", "hash"),
    ),
    _e(
        "marketplace_prices_averages",
        "marketplace_prices_averages",
        "MarketplacePriceAverage",
        ttl=HOUR,
        params=(
            "id_item",
            "id_category",
            "item_uuid",
            "item_name",
            "operation",
            "quality_tier",
            "currency",
            "game_version",
        ),
        requires=("any", "id_item", "id_category", "item_uuid", "item_name"),
        multi=("id_item",),
    ),
    _e(
        "marketplace_prices_averages_all",
        "marketplace_prices_averages_all",
        "MarketplacePriceAverageSummary",
        ttl=HOUR,
    ),
    _e(
        "marketplace_prices_history",
        "marketplace_prices_history",
        "MarketplacePriceHistory",
        ttl=HOUR,
        params=(
            "id_item",
            "id_listing",
            "id_terminal",
            "id_star_system",
            "id_category",
            "item_uuid",
            "item_name",
            "operation",
            "quality_tier",
            "currency",
            "game_version",
            "date_start",
            "date_end",
        ),
        requires=(
            "any",
            "id_item",
            "id_listing",
            "id_terminal",
            "id_star_system",
            "id_category",
            "item_uuid",
            "item_name",
        ),
        multi=("id_item",),
    ),
    _e(
        "marketplace_trends",
        "marketplace_trends",
        "MarketplaceTrend",
        ttl=HOUR,
        params=("id_item", "item_name", "id_category", "currency", "quality_tier"),
    ),
    # -- refineries -------------------------------------------------------------
    _e("refineries_methods", "refineries_methods", "RefineryMethod", ttl=DAY),
    _e("refineries_yields", "refineries_yields", "RefineryYield", ttl=DAY),
    _e("refineries_capacities", "refineries_capacities", "RefineryCapacity", ttl=DAY),
    _e("refineries_audits", "refineries_audits", "RefineryAudit", ttl=DAY),
    # -- currencies ---------------------------------------------------------
    _e("currencies_index", "currencies_index", "CurrencyIndex", ttl=DAY, params=("currency",)),
    _e(
        "currencies_index_history",
        "currencies_index_history",
        "CurrencyIndexSnapshot",
        ttl=DAY,
        params=("currency", "date_from", "date_to"),
    ),
    # -- game versions --------------------------------------------------------
    _e("game_versions", "game_versions", "GameVersions", ttl=DAY, single=True),
    _e("game_versions_all", "game_versions_all", "GameVersionEntry", ttl=DAY),
    # -- polls ------------------------------------------------------------------
    _e(
        "polls",
        "polls",
        "Poll",
        params=(
            "id",
            "id_item",
            "id_vehicle",
            "id_commodity",
            "status",
            "category",
            "sort",
        ),
    ),
    _e("polls_audit", "polls_audit", "PollAuditEntry", params=("id",), requires=("all", "id")),
    # -- crew -------------------------------------------------------------------
    _e(
        "crew",
        "crew",
        "CrewMember",
        params=(
            "specialization",
            "day_availability",
            "time_availability",
            "languages",
            "archetypes",
            "timezone",
            "username",
        ),
        requires=("all", "specialization"),
    ),
    # -- data / meta --------------------------------------------------------
    _e("data_parameters", "data_parameters", "DataParameters", ttl=DAY, single=True),
    _e(
        "data_monitor",
        "data_monitor",
        "DataMonitorEntry",
        auth=TOKEN,
        ttl=HOUR,
        params=("type", "id_star_system", "id_faction"),
    ),
    _e(
        "data_info",
        "data_info",
        "DataInfo",
        auth=TOKEN,
        params=("id", "type", "id_terminal", "status", "username", "limit"),
    ),
    # -- user -----------------------------------------------------------------
    _e(
        "user",
        "user",
        "User",
        params=("username",),
        requires=("any", "username"),
        single=True,
    ),
    _e("user_notifications", "user_notifications", "UserNotification", auth=SECRET),
    _e("user_trades", "user_trades", "UserTrade", auth=SECRET),
    _e("user_refineries_jobs", "user_refineries_jobs", "UserRefineryJob", auth=SECRET),
    _e("fleet", "fleet", "FleetVehicle", auth=SECRET),
    _e("wallet_balance", "wallet_balance", "WalletBalance", auth=SECRET, single=True),
    _e(
        "organizations",
        "organizations",
        "Organization",
        auth=TOKEN,
        params=("id_organization", "slug"),
        requires=("any", "id_organization", "slug"),
        single=True,
    ),
    _e("release_notes", "release_notes", "ReleaseNote", ttl=DAY),
)

ENDPOINTS: dict[str, Endpoint] = {e.name: e for e in _ALL}
