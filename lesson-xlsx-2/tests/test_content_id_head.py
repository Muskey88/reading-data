def test_content_id_head():
    from pandas.util.testing import assert_frame_equal

    content_id_head = pd.DataFrame({'Content_ID': [101, 101, 101, 102, 101],
                                'Content_Rating': ['Everyone', 'Everyone', 'Everyone', 'Teen', 'Everyone']})

    assert_frame_equal(content_id.head(), content_id_head)
