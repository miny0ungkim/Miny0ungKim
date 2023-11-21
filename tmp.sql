with tmp as (
    select sum(amount) over(partition by order_id oder by click_date)
    from crm c join )