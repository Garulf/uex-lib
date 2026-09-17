"""Friendly method names for each namespace, mapping to endpoint names."""

from __future__ import annotations

NAMESPACES: dict[str, dict[str, str]] = {
    "commodities": {
        "list": "commodities",
        "prices": "commodities_prices",
        "prices_all": "commodities_prices_all",
        "prices_history": "commodities_prices_history",
        "alerts": "commodities_alerts",
        "averages": "commodities_averages",
        "ranking": "commodities_ranking",
        "raw_averages": "commodities_raw_averages",
        "raw_prices": "commodities_raw_prices",
        "raw_prices_all": "commodities_raw_prices_all",
        "routes": "commodities_routes",
        "status": "commodities_status",
    },
    "fuel": {
        "prices": "fuel_prices",
        "prices_all": "fuel_prices_all",
    },
    "items": {
        "list": "items",
        "attributes": "items_attributes",
        "prices": "items_prices",
        "prices_all": "items_prices_all",
    },
    "categories": {
        "list": "categories",
        "attributes": "categories_attributes",
    },
    "vehicles": {
        "list": "vehicles",
        "loaners": "vehicles_loaners",
        "prices": "vehicles_prices",
        "purchase_prices": "vehicles_purchases_prices",
        "purchase_prices_all": "vehicles_purchases_prices_all",
        "rental_prices": "vehicles_rentals_prices",
        "rental_prices_all": "vehicles_rentals_prices_all",
    },
    "terminals": {
        "list": "terminals",
        "distances": "terminals_distances",
    },
    "universe": {
        "star_systems": "star_systems",
        "planets": "planets",
        "moons": "moons",
        "orbits": "orbits",
        "orbit_distances": "orbits_distances",
        "space_stations": "space_stations",
        "cities": "cities",
        "outposts": "outposts",
        "poi": "poi",
        "jump_points": "jump_points",
        "jurisdictions": "jurisdictions",
        "factions": "factions",
        "companies": "companies",
        "contacts": "contacts",
        "contracts": "contracts",
    },
    "marketplace": {
        "listings": "marketplace_listings",
        "averages": "marketplace_averages",
        "averages_all": "marketplace_averages_all",
        "prices_averages": "marketplace_prices_averages",
        "prices_averages_all": "marketplace_prices_averages_all",
        "prices_history": "marketplace_prices_history",
        "trends": "marketplace_trends",
        "favorites": "marketplace_favorites",
        "negotiations": "marketplace_negotiations",
        "negotiation_messages": "marketplace_negotiations_messages",
    },
    "refineries": {
        "methods": "refineries_methods",
        "yields": "refineries_yields",
        "capacities": "refineries_capacities",
        "audits": "refineries_audits",
    },
    "currencies": {
        "index": "currencies_index",
        "index_history": "currencies_index_history",
    },
    "game_versions": {
        "current": "game_versions",
        "all": "game_versions_all",
    },
    "polls": {
        "list": "polls",
        "audit": "polls_audit",
    },
    "crew": {
        "search": "crew",
    },
    "data": {
        "parameters": "data_parameters",
        "monitor": "data_monitor",
        "info": "data_info",
    },
    "user": {
        "get": "user",
        "notifications": "user_notifications",
        "trades": "user_trades",
        "refinery_jobs": "user_refineries_jobs",
        "fleet": "fleet",
        "wallet_balance": "wallet_balance",
    },
    "organizations": {
        "get": "organizations",
    },
    "release_notes": {
        "list": "release_notes",
    },
}
