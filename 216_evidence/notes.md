## Notes

#### Evidence Notes
- in `0.log` there are a lot of errors about files not existing
- nothing to weird in `1-python.log`, just a bunch of python linting about code
- in `email_record.log` multiple emails containing zip files for new software and office financials
- in `index.log` you have a couple errors and stack-trace, including
> About(root_id=u'0ADOxB8YHOaFTUk9PVA', email_address=u'user@mail.org', quota_bytes_total=16106127360L, quota_bytes_used_aggregate=297841981L, quota_bytes_used_in_trash=3908767L, quota_type=<QuotaType.LIMITED: 1>, picture_url=u'https://lh6.googleusercontent.com/-Xx6fIkmXiUo/AAAAAAAAAAI/AAAAAAAAAAs/zSQHa8tVkog/s64/photo.jpg', apps_domain='')
> 2019-02-12 06:01:41,917 -0800 INFO pid=9348 21332:LaunchThreads   proxy_manager.py:141 Exception while auto resolving proxy.
- in the `loginscript.log` there are a few errors, but nothing seems too strange.

### Downloads Notes
- it appears all the links from the email have been downloaded including the two zip files.
- updates folder is the culprit most likely it has a lot of python files.

##### Downloads/clean
I have made a subdirectory `clean` in `Downloads` for files that seem fine.
