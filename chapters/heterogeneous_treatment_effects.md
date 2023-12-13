# Heterogeneous treatment effects

- Based on @bojinov2020avoid

- Focusing only on mean outcomes can be detrimental in the long-term, especially in contexts where metrics are driven heavily by a small subset of superusers.

- In such cases, focusing on the average effectively builds products for superusers, which can be a missed opportunity because increasing the engagement of infrequent users is often one of the largest opportunities for growth.

- Solutions:

    - Use metrics and approaches that reflect the needs of different customer segments (e.g. specially designed metric, [interleaving](https://netflixtechblog.com/interleaving-in-online-experiments-at-netflix-a04ee392ec55))

    - Measure impact across different levels of technical access (e.g. slice experiment results based on type of device (latest or older), speed of internet connection (check percentiles))

    - Account for group-specific behaviour (slice experiment results by country, main individual characteristics, and track share of top-line metrics contributed by top 1% of users)

    - Segment key markets (e.g. build versions of the product suitable for particular needs -- e.g. LinkedIn Light built to cater for Indian users on slower 3G networks).

