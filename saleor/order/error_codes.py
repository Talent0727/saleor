from enum import Enum


class OrderErrorCode(Enum):
    BILLING_ADDRESS_NOT_SET = "billing_address_not_set"
    CANNOT_CANCEL_FULFILLMENT = "cannot_cancel_fulfillment"
    CANNOT_CANCEL_ORDER = "cannot_cancel_order"
    CANNOT_DELETE = "cannot_delete"
    CANNOT_DISCOUNT = "cannot_discount"
    CANNOT_REFUND = "cannot_refund"
    CANNOT_FULFILL_UNPAID_ORDER = "cannot_fulfill_unpaid_order"
    CAPTURE_INACTIVE_PAYMENT = "capture_inactive_payment"
    GIFT_CARD_LINE = "gift_card_line"
    NOT_EDITABLE = "not_editable"
    FULFILL_ORDER_LINE = "fulfill_order_line"
    GRAPHQL_ERROR = "graphql_error"
    INVALID = "invalid"
    PRODUCT_NOT_PUBLISHED = "product_not_published"
    PRODUCT_UNAVAILABLE_FOR_PURCHASE = "product_unavailable_for_purchase"
    NOT_FOUND = "not_found"
    ORDER_NO_SHIPPING_ADDRESS = "order_no_shipping_address"
    PAYMENT_ERROR = "payment_error"
    PAYMENT_MISSING = "payment_missing"
    TRANSACTION_ERROR = "transaction_error"
    REQUIRED = "required"
    SHIPPING_METHOD_NOT_APPLICABLE = "shipping_method_not_applicable"
    SHIPPING_METHOD_REQUIRED = "shipping_method_required"
    TAX_ERROR = "tax_error"
    UNIQUE = "unique"
    VOID_INACTIVE_PAYMENT = "void_inactive_payment"
    ZERO_QUANTITY = "zero_quantity"
    INVALID_QUANTITY = "invalid_quantity"
    INSUFFICIENT_STOCK = "insufficient_stock"
    DUPLICATED_INPUT_ITEM = "duplicated_input_item"
    NOT_AVAILABLE_IN_CHANNEL = "not_available_in_channel"
    CHANNEL_INACTIVE = "channel_inactive"


class OrderGrantRefundCreateErrorCode(Enum):
    GRAPHQL_ERROR = "graphql_error"
    NOT_FOUND = "not_found"


class OrderGrantRefundUpdateErrorCode(Enum):
    GRAPHQL_ERROR = "graphql_error"
    NOT_FOUND = "not_found"
    REQUIRED = "required"
